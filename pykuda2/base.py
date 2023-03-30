from abc import ABC, abstractmethod
from dataclasses import dataclass
from enum import Enum
from json import JSONDecodeError
from typing import Optional, Union
from httpx import codes as HTTP_STATUS_CODE

__version__ = "0.1.0"

from uuid import uuid4

import httpx

from pykuda2.exceptions import (
    UnsupportedHTTPMethodException,
    ConnectionException,
    InvalidResponseException,
    TokenException,
)


@dataclass
class APIResponse:
    status_code: int
    status: Optional[str]
    message: Optional[str]
    data: Optional[dict]
    raw: Union[list, dict]


class HTTPMethod(str, Enum):
    GET = "GET"
    POST = "POST"
    PUT = "PUT"
    PATCH = "PATCH"
    DELETE = "DELETE"
    OPTIONS = "OPTIONS"
    HEAD = "HEAD"


class Mode(str, Enum):
    DEVELOPMENT = "development"
    PRODUCTION = "production"


class ServiceType(str, Enum):
    """
    An enumeration of Service Types Provided by Kuda

    Attributes:
        ADMIN_CREATE_VIRTUAL_ACCOUNT: Create a virtual account under your main account
        ADMIN_VIRTUAL_ACCOUNTS: Get all Virtual account
        ADMIN_UPDATE_VIRTUAL_ACCOUNT: Update virtual account details
        ADMIN_DISABLE_VIRTUAL_ACCOUNT: Deactivate a virtual account
        ADMIN_ENABLE_VIRTUAL_ACCOUNT: Reactivate a virtual account
        RETRIEVE_SINGLE_VIRTUAL_ACCOUNT: Retrieve the details on a created virtual account
        BANK_LIST: Get a list of all banks
        NAME_ENQUIRY: Retrieve the name linked to a bank account
        SINGLE_FUND_TRANSFER: Transfer money from your main account
        VIRTUAL_ACCOUNT_FUND_TRANSFER: Transfer money from a virtual account
        TRANSACTION_STATUS_QUERY: Get the status of a bank transfer
        RETRIEVE_VIRTUAL_ACCOUNT_BALANCE: Retrieve the account balance on a virtual account
        ADMIN_MAIN_ACCOUNT_TRANSACTIONS: Get all transactions on your account
        ADMIN_MAIN_ACCOUNT_FILTERED_TRANSACTIONS: Get a date filtered range of transactions on your account
        ADMIN_VIRTUAL_ACCOUNT_TRANSACTIONS: Get all transactions on a virtual account
        ADMIN_VIRTUAL_ACCOUNT_FILTERED_TRANSACTIONS: Get a date filtered range of transactions on a virtual account
        FUND_VIRTUAL_ACCOUNT: Transfer money from your main acount to your virtual account
        WITHDRAW_VIRTUAL_ACCOUNT: Transfer money from your virtual account to your main account
        UPDATE_VIRTUAL_ACCOUNT_LIMIT: Updated transfer limits up to N5,000,000 daily on your most critical virtual accounts
        FUND_TRANSFER_INSTRUCTION: Instruction for single transaction above the limit of One (1) million naira
        SEARCH_FUND_TRANSFER_INSTRUCTION: Search for transfer instructions and return the status of the transaction
        RETRIEVE_TRANSACTION_LOGS: Fetch all transaction from logs
        GET_GIFT_CARD: gets a list of all gift card supported
        ADMIN_BUY_GIFT_CARD: purchase gift card from admin account
        BUY_GIFT_CARD: purchase gift card from virtual account
        GIFT_CARD_TSQ: status of all gift cards purchased

    """

    ADMIN_CREATE_VIRTUAL_ACCOUNT = "ADMIN_CREATE_VIRTUAL_ACCOUNT"
    ADMIN_VIRTUAL_ACCOUNTS = "ADMIN_VIRTUAL_ACCOUNTS"
    ADMIN_UPDATE_VIRTUAL_ACCOUNT = "ADMIN_UPDATE_VIRTUAL_ACCOUNT"
    ADMIN_DISABLE_VIRTUAL_ACCOUNT = "ADMIN_DISABLE_VIRTUAL_ACCOUNT"
    ADMIN_ENABLE_VIRTUAL_ACCOUNT = "ADMIN_ENABLE_VIRTUAL_ACCOUNT"
    RETRIEVE_SINGLE_VIRTUAL_ACCOUNT = "RETRIEVE_SINGLE_VIRTUAL_ACCOUNT"
    BANK_LIST = "BANK_LIST"
    NAME_ENQUIRY = "NAME_ENQUIRY"
    SINGLE_FUND_TRANSFER = "SINGLE_FUND_TRANSFER"
    VIRTUAL_ACCOUNT_FUND_TRANSFER = "VIRTUAL_ACCOUNT_FUND_TRANSFER"
    TRANSACTION_STATUS_QUERY = "TRANSACTION_STATUS_QUERY"
    RETRIEVE_VIRTUAL_ACCOUNT_BALANCE = "RETRIEVE_VIRTUAL_ACCOUNT_BALANCE"
    ADMIN_MAIN_ACCOUNT_TRANSACTIONS = "ADMIN_MAIN_ACCOUNT_TRANSACTIONS"
    ADMIN_MAIN_ACCOUNT_FILTERED_TRANSACTIONS = "ADMIN_MAIN_ACCOUNT_FILTERED_TRANSACTIONS"
    ADMIN_VIRTUAL_ACCOUNT_TRANSACTIONS = "ADMIN_VIRTUAL_ACCOUNT_TRANSACTIONS"
    ADMIN_VIRTUAL_ACCOUNT_FILTERED_TRANSACTIONS = "ADMIN_VIRTUAL_ACCOUNT_FILTERED_TRANSACTIONS"
    FUND_VIRTUAL_ACCOUNT = "FUND_VIRTUAL_ACCOUNT"
    WITHDRAW_VIRTUAL_ACCOUNT = "WITHDRAW_VIRTUAL_ACCOUNT"
    UPDATE_VIRTUAL_ACCOUNT_LIMIT = "UPDATE_VIRTUAL_ACCOUNT_LIMIT"
    FUND_TRANSFER_INSTRUCTION = "FUND_TRANSFER_INSTRUCTION"
    SEARCH_FUND_TRANSFER_INSTRUCTION = "SEARCH_FUND_TRANSFER_INSTRUCTION"
    RETRIEVE_TRANSACTION_LOGS = "RETRIEVE_TRANSACTION_LOGS"
    GET_GIFT_CARD = " GET_GIFT_CARD"
    ADMIN_BUY_GIFT_CARD = "ADMIN_BUY_GIFT_CARD"
    BUY_GIFT_CARD = "BUY_GIFT_CARD"
    GIFT_CARD_TSQ = "GIFT_CARD_TSQ"







class AbstractAPIWrapper(ABC):
    def __init__(self, email: str, api_key: str, mode=Mode.DEVELOPMENT):
        self.mode = mode
        self.email = email
        self.api_key = api_key
        self._token: Optional[str] = None

    @property
    @abstractmethod
    def token(self) -> str:
        ...

    @property
    @abstractmethod
    def headers(self) -> dict:
        ...

    @property
    def base_headers(self) -> dict:
        return {
            "accept": "application/json; charset=utf-8",
            "content-type": "application/json",
            "user-agent": f"PyKuda {__version__}",
        }

    @property
    def base_url(self) -> str:
        return {
            Mode.DEVELOPMENT: "http://kuda-openapi-uat.kudabank.com/v2.1",
            Mode.PRODUCTION: "https://kuda-openapi.kuda.com/v2.1",
        }[self.mode]

    @abstractmethod
    def api_call(self, service_type: ServiceType, data: dict, method=HTTPMethod.POST):
        ...

    def _parse_call_kwargs(self, service_type: ServiceType, data: Optional[dict]=None) -> dict:
        payload = {
            "servicetype": service_type,
            "requestref": str(uuid4()),
            "data": data,
        }
        if not data:
            payload.pop('data', None)
        return {
            "url": self.base_url,
            "json": payload,
            "headers": self.headers,
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


class APIWrapper(AbstractAPIWrapper):
    def __init__(self, email: str, api_key: str, mode=Mode.DEVELOPMENT):
        super().__init__(email=email, api_key=api_key, mode=mode)

    @property
    def token(self) -> str:
        if self._token:
            return self._token
        else:
            token_url = f"{self.base_url}/Account/GetToken"
            auth_data = {"email": self.email, "apiKey": self.api_key}
            try:
                response = httpx.post(
                    url=token_url, json=auth_data, headers=self.base_headers
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
    def headers(self) -> dict:
        return {**self.base_headers, "authorization": f"Bearer {self.token}"}

    def api_call(self, service_type: ServiceType, data: Optional[dict]=None, method=HTTPMethod.POST):

        http_method_call_kwargs = self._parse_call_kwargs(
            service_type=service_type, data=data
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
        except httpx.ConnectTimeout:
            raise ConnectionException("Server refused to respond")


class AsyncAPIWrapper(AbstractAPIWrapper):
    def __init__(self, email: str, api_key: str, mode=Mode.DEVELOPMENT):
        super().__init__(email=email, api_key=api_key, mode=mode)

    @property
    async def token(self) -> str:
        if self._token:
            return self._token
        else:
            token_url = f"{self.base_url}/Account/GetToken"
            auth_data = {"email": self.email, "apiKey": self.api_key}
            try:
                async with httpx.AsyncClient() as client:
                    response = await client.post(
                        url=token_url, json=auth_data, headers=self.base_headers
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
    async def headers(self) -> dict:
        return {**self.base_headers, "authorization": f"Bearer {await self.token}"}

    async def api_call(
        self, service_type: ServiceType, data: dict, method=HTTPMethod.POST
    ):
        http_method_call_kwargs = await self._parse_call_kwargs(
            service_type=service_type, data=data
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
            except httpx.ConnectTimeout:
                raise ConnectionException("Server refused to respond")
            return self._parse_response(response)

    async def _parse_call_kwargs(self, service_type: ServiceType, data: dict) -> dict:
        payload = {
            "ServiceType": service_type,
            "RequestRef": str(uuid4()),
            "Data": data,
        }
        return {
            "url": self.base_url,
            "json": payload,
            "headers": await self.headers,
        }
