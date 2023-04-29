from abc import ABC, abstractmethod
from json import JSONDecodeError
from typing import Optional
from httpx import codes as HTTP_STATUS_CODE

__version__ = "0.1.0"


import httpx

from pykuda2.exceptions import (
    UnsupportedHTTPMethodException,
    ConnectionException,
    InvalidResponseException,
    TokenException,
)
from pykuda2.utils import APIResponse, HTTPMethod, Mode, ServiceType, generate_number

REFERENCE_NUMBER_LENGTH = 10


class AbstractAPIWrapper(ABC):
    def __init__(self, email: str, api_key: str, mode=Mode.DEVELOPMENT):
        """Instantiates the APIWrapper.

        Args:
            email: The email address of your Kuda account with access to an apiKey.
            api_key: Your Kuda apiKey.
            mode: The mode you desire to use the wrapper in (development or production).
        """
        self._mode = mode
        self._email = email
        self._api_key = api_key
        self._saved_token: Optional[str] = None

    @property
    @abstractmethod
    def _token(self) -> str:
        """Returns the access token gotten.

        It performs authentication with `self.email` and `self.api_key` to get it"""
        ...

    @property
    @abstractmethod
    def _headers(self) -> dict:
        """Returns the headers with authorization header included.

        It returns the headers used in making requests with the inclusion of an authorization header"""
        ...

    @property
    def _base_headers(self) -> dict:
        """Returns the headers without authorization header included.

        It returns the headers used in making endpoint requests with the exclusion of the authorization header"""
        return {
            "accept": "application/json; charset=utf-8",
            "content-type": "application/json",
            "user-agent": f"PyKuda {__version__}",
        }

    @property
    def _base_url(self) -> str:
        """Returns the base url.

        The url returned depends on the mode in which the class was instantiated."""
        return {
            Mode.DEVELOPMENT: "https://kuda-openapi-uat.kudabank.com/v2.1",
            Mode.PRODUCTION: "https://kuda-openapi.kuda.com/v2.1",
        }[self._mode]

    @abstractmethod
    def _api_call(
        self,
        service_type: ServiceType,
        data: dict,
        method=HTTPMethod.POST,
        endpoint_path: Optional[str] = None,
        request_reference: Optional[str] = None,
    ):
        """Allows sending to request to Kuda endpoint's based on `service_type` and `endpoint_path`.

        Most of Kuda APIs use a single url architecture in which the route is determined by the
        content of the request in this case the `service_type`, for these type of endpoints, the
        endpoint url is just the `base_url`. There are also edge cases where  this rule does not apply.
        Take for example an end point `https://kuda-openapi-uat.kudabank.com/v2.1/Account/GetToken`
        to send request to endpoints like this, only `/Account/GetToken` needs to be passed to
        the `endpoint_path` since the `base_url` is `https://kuda-openapi-uat.kudabank.com/v2.1`
        by default depending on mode.

        Args:
            service_type: The Kuda service we're interested in.
            data: The data we're sending to the endpoint.
            method: The HTTP method the endpoint accepts
            endpoint_path: This is optional and only required by endpoints that don't comply with the
                single url architecture. Only the endpoint path should be provided as a string.
            request_reference: A unique identifier for each reqeust. it is auto generated if
                this parameter is not provided.
        Returns:
            An `APIResponse` which is basically just a dataclass containing the data returned
            by the server as result of calling this function.
        Raises:
            UnsupportedHTTPMethodException: when an invalid HTTP verb is provided.
            ConnectionException: when the request times out or in the absence of an internet connection.
        """
        ...

    def _parse_call_kwargs(
        self,
        service_type: ServiceType,
        data: Optional[dict] = None,
        endpoint_path: Optional[str] = None,
        request_reference: Optional[str] = None,
        exclude_auth_header=False,
    ) -> dict:
        payload = {
            "servicetype": service_type,
            "requestref": request_reference
            or str(generate_number(REFERENCE_NUMBER_LENGTH)),
            "data": data,
        }
        if not data:
            payload.pop("data", None)
        if service_type == ServiceType.NO_OP:
            payload.pop("servicetype", None)
        return {
            "url": self._base_url + endpoint_path
            if endpoint_path is not None
            else self._base_url,
            "json": payload,
            "headers": self._headers if not exclude_auth_header else self._base_headers,
        }

    def _parse_response(self, response: httpx.Response) -> APIResponse:
        try:
            response_body = response.json()
            return APIResponse(
                status_code=response.status_code,
                status=response_body.get("Status") or response_body.get("status"),
                message=response_body.get("Message") or response_body.get("message"),
                data=response_body.get("Data") or response_body.get("data"),
                raw=response_body,
            )
        except JSONDecodeError:
            raise InvalidResponseException(
                f"Unable to decode response. STATUS_CODE: {response.status_code}"
            )


class BaseAPIWrapper(AbstractAPIWrapper):
    """A base class from which synchronous API wrappers inherit from.

    It provides functionalities required to make requests to Kuda API

    Args:
        email: The email address of your Kuda account with access to an apiKey
        api_key: Your Kuda apiKey
        mode: The mode you desire to use the wrapper in (development or production)
    """

    def __init__(self, email: str, api_key: str, mode=Mode.DEVELOPMENT):
        super().__init__(email=email, api_key=api_key, mode=mode)

    @property
    def _token(self) -> str:
        if self._saved_token:
            return self._saved_token
        else:
            token_url = f"{self._base_url}/Account/GetToken"
            auth_data = {"email": self._email, "apiKey": self._api_key}
            try:
                response = httpx.post(
                    url=token_url, json=auth_data, headers=self._base_headers
                )
            except httpx.ConnectError:
                raise ConnectionException(
                    "Unable to connect to server. Please ensure you have an internet connection"
                )
            except httpx.ConnectTimeout:
                raise ConnectionException("Server refused to respond")
            if response.status_code == HTTP_STATUS_CODE.OK:
                return response.text
            raise TokenException(
                "Unable to get access token, It's likely that you provided an invalid credential "
                "or your apiKey has expired. You can always generate a new apiKey "
                "from your developer account"
            )

    @property
    def _headers(self) -> dict:
        return {**self._base_headers, "authorization": f"Bearer {self._token}"}

    def _api_call(
        self,
        service_type: ServiceType,
        data: Optional[dict] = None,
        method=HTTPMethod.POST,
        endpoint_path: Optional[str] = None,
        request_reference: Optional[str] = None,
        exclude_auth_header=False,
    ):

        http_method_call_kwargs = self._parse_call_kwargs(
            service_type=service_type,
            data=data,
            endpoint_path=endpoint_path,
            request_reference=request_reference,
            exclude_auth_header=exclude_auth_header,
        )
        http_methods_mapping = {
            HTTPMethod.GET: httpx.get,
            HTTPMethod.POST: httpx.post,
            HTTPMethod.PUT: httpx.put,
            HTTPMethod.PATCH: httpx.patch,
            HTTPMethod.DELETE: httpx.delete,
            HTTPMethod.OPTIONS: httpx.options,
            HTTPMethod.HEAD: httpx.head,
        }
        http_method_callable = http_methods_mapping.get(method)
        if not http_method_callable:
            raise UnsupportedHTTPMethodException(
                f"{method} is not a supported HTTP method"
            )
        try:
            response = http_method_callable(**http_method_call_kwargs)
            return self._parse_response(response)
        except httpx.ConnectError:
            raise ConnectionException(
                "Unable to connect to server. Please ensure you have an internet connection"
            )
        except (httpx.ConnectTimeout, httpx.ReadTimeout):
            raise ConnectionException("Server refused to respond")


class BaseAsyncAPIWrapper(AbstractAPIWrapper):
    """A base class from which asynchronous API wrappers inherit from.

    It provides functionalities required to make requests to Kuda API

    Args:
        email: The email address of your Kuda account with access to an apiKey
        api_key: Your Kuda apiKey
        mode: The mode you desire to use the wrapper in (development or production)
    """

    def __init__(self, email: str, api_key: str, mode=Mode.DEVELOPMENT):
        super().__init__(email=email, api_key=api_key, mode=mode)

    @property
    async def _token(self) -> str:
        if self._saved_token:
            return self._saved_token
        else:
            token_url = f"{self._base_url}/Account/GetToken"
            auth_data = {"email": self._email, "apiKey": self._api_key}
            try:
                async with httpx.AsyncClient() as client:
                    response = await client.post(
                        url=token_url, json=auth_data, headers=self._base_headers
                    )
            except httpx.ConnectError:
                raise ConnectionException(
                    "Unable to connect to server. Please ensure you have an internet connection"
                )
            except (httpx.ConnectTimeout, httpx.ReadTimeout):
                raise ConnectionException("Server refused to respond")
            if response.status_code == HTTP_STATUS_CODE.OK:
                return response.text
            raise TokenException(
                "Unable to get access token, It's likely that you provided an invalid credential "
                "or your apiKey has expired. You can always generate a new apiKey "
                "from your developer account"
            )

    @property
    async def _headers(self) -> dict:
        return {**self._base_headers, "authorization": f"Bearer {await self._token}"}

    async def _api_call(
        self,
        service_type: ServiceType,
        data: Optional[dict] = None,
        method=HTTPMethod.POST,
        endpoint_path: Optional[str] = None,
        request_reference: Optional[str] = None,
        exclude_auth_header=False,
    ):
        http_method_call_kwargs = await self._parse_call_kwargs_async(
            service_type=service_type,
            data=data,
            endpoint_path=endpoint_path,
            request_reference=request_reference,
            exclude_auth_header=exclude_auth_header,
        )
        async with httpx.AsyncClient() as client:
            http_method_callable = getattr(client, method.value.lower(), None)
            if not http_method_callable:
                raise UnsupportedHTTPMethodException(
                    f"{method} is not a supported HTTP method"
                )
            try:
                response = await http_method_callable(**http_method_call_kwargs)
            except httpx.ConnectError:
                raise ConnectionException(
                    "Unable to connect to server. Please ensure you have an internet connection"
                )
            except (httpx.ConnectTimeout, httpx.ReadTimeout):
                raise ConnectionException("Server refused to respond")
            return self._parse_response(response)

    async def _parse_call_kwargs_async(
        self,
        service_type: ServiceType,
        data: Optional[dict],
        endpoint_path: Optional[str] = None,
        request_reference: Optional[str] = None,
        exclude_auth_header=False,
    ) -> dict:
        payload = {
            "ServiceType": service_type,
            "RequestRef": request_reference
            or str(generate_number(REFERENCE_NUMBER_LENGTH)),
            "Data": data,
        }
        if not data:
            payload.pop("data", None)
        if service_type == ServiceType.NO_OP:
            payload.pop("ServiceType", None)
        return {
            "url": self._base_url + endpoint_path
            if endpoint_path is not None
            else self._base_url,
            "json": payload,
            "headers": await self._headers
            if not exclude_auth_header
            else self._base_headers,
        }
