from typing import Optional

from pykuda2.base import BaseAPIWrapper
from pykuda2.utils import ServiceType, APIResponse


class Account(BaseAPIWrapper):
    def create_virtual_account(
        self,
        email: str,
        phone_number: str,
        last_name: str,
        first_name: str,
        middle_name: str,
        business_name: str,
        tracking_reference: str,
        request_reference: Optional[str] = None,
    ) -> APIResponse:
        """Creates a new virtual account for customers.

        Args:
            email: customer's email address.
            phone_number: customer's phone number.
            last_name: customer's last name.
            first_name: customer's first name.
            middle_name: customer's middle name.
            business_name: customer's business name.
            tracking_reference: a unique identifier for the account to be created.
            request_reference: a unique identifier for this api call.
                it is automatically generated if not provided.

        Returns:
            An `APIResponse` which is basically just a dataclass containing the data returned by the server as result
                of calling this function.

        Raises:
            ConnectionException: when the request times out or in the absence of an internet connection.
        """
        data = {
            "email": email,
            "phoneNumber": phone_number,
            "lastName": last_name,
            "firstName": first_name,
            "middleName": middle_name,
            "businessName": business_name,
            "trackingReference": tracking_reference,
        }
        return self._api_call(
            service_type=ServiceType.ADMIN_CREATE_VIRTUAL_ACCOUNT,
            data=data,
            request_reference=request_reference,
        )

    def update_virtual_account(
        self,
        tracking_reference: str,
        first_name: Optional[str] = None,
        last_name: Optional[str] = None,
        email: Optional[str] = None,
        request_reference: Optional[str] = None,
    ) -> APIResponse:
        """Modifies a virtual account data.

        Good to know: For context, you cannot alter the phone number of the customer.
        You may only alter either the first name/last name or email address tied to
        the account information.
        Do not update the name and the email address together on a single request.

        Args:
            tracking_reference: The customer's unique identifier.
            first_name: The new first name the customer's first name should be updated to if provided.
            last_name: The new last name the customer's last name should be updated to if provided.
            email: The new email address the customer's email address should be updated to if provided.
            request_reference: a unique identifier for this api call.
                it is automatically generated if not provided.

        Returns:
            An `APIResponse` which is basically just a dataclass containing the data returned by the server as result
                of calling this function.

        Raises:
            ConnectionException: when the request times out or in the absence of an internet connection.
            ValueError: If none of the optional parameters is provided.
        """
        if not any([first_name, last_name, email]):
            raise ValueError(
                "At least one of the parameters `first_name`, `last_name` or `email` must be provided"
            )
        data = {
            "trackingReference": tracking_reference,
            "firstName": first_name,
            "lastName": last_name,
            "email": email,
        }
        if not first_name:
            data.pop("firstName")
        if not last_name:
            data.pop("lastName")
        if not email:
            data.pop("email")
        return self._api_call(
            service_type=ServiceType.ADMIN_UPDATE_VIRTUAL_ACCOUNT,
            data=data,
            request_reference=request_reference,
        )

    def get_virtual_accounts(
        self, page_size: int, page_number: int, request_reference: Optional[str] = None
    ) -> APIResponse:
        """Retrieves your existing virtual accounts.

        Args:
            page_size: This specifies the number of virtual accounts to be retrieved.
            page_number: This specifies the index of the paginated results retrieved.
            request_reference: a unique identifier for this api call.
                it is automatically generated if not provided.

        Returns:
            An `APIResponse` which is basically just a dataclass containing the data returned by the server as result
                of calling this function.

        Raises:
            ConnectionException: when the request times out or in the absence of an internet connection.
        """
        data = {
            "PageSize": page_size,
            "PageNumber": page_number,
        }
        return self._api_call(
            service_type=ServiceType.ADMIN_VIRTUAL_ACCOUNTS,
            data=data,
            request_reference=request_reference,
        )

    def get_virtual_account(
        self, tracking_reference: str, request_reference: Optional[str] = None
    ) -> APIResponse:
        """Retrieves an existing virtual account.

        Args:
            tracking_reference: the unique identifier tied to the account to be retrieved.
            request_reference: a unique identifier for this api call.
                it is automatically generated if not provided.

        Returns:
            An `APIResponse` which is basically just a dataclass containing the data returned by the server as result
                of calling this function.

        Raises:
            ConnectionException: when the request times out or in the absence of an internet connection.
        """
        data = {
            "trackingReference": tracking_reference,
        }
        return self._api_call(
            service_type=ServiceType.ADMIN_RETRIEVE_SINGLE_VIRTUAL_ACCOUNT,
            data=data,
            request_reference=request_reference,
        )

    def disable_virtual_account(
        self, tracking_reference: str, request_reference: Optional[str] = None
    ) -> APIResponse:
        """Disables a user’s virtual static account.

        Kuda encourages Admins and account managers to review accounts and transactions
        frequently. This will avoid situations where a user has an over bloated customer
        database without real customers or helping to reduce the menace of fraudulent transactions.

        Args:
            tracking_reference: the unique identifier tied to the account to be disabled.
            request_reference: a unique identifier for this api call.
                it is automatically generated if not provided.

        Returns:
            An `APIResponse` which is basically just a dataclass containing the data returned by the server as result
                of calling this function.

        Raises:
            ConnectionException: when the request times out or in the absence of an internet connection.
        """
        data = {
            "trackingReference": tracking_reference,
        }
        return self._api_call(
            service_type=ServiceType.ADMIN_DISABLE_VIRTUAL_ACCOUNT,
            data=data,
            request_reference=request_reference,
        )

    def enable_virtual_account(
        self, tracking_reference: str, request_reference: Optional[str] = None
    ) -> APIResponse:
        """Enables a user’s virtual static account.

        Args:
            tracking_reference: the unique identifier tied to the account to be enabled.
            request_reference: a unique identifier for this api call.
                it is automatically generated if not provided.

        Returns:
            An `APIResponse` which is basically just a dataclass containing the data returned by the server as result
                of calling this function.

        Raises:
            ConnectionException: when the request times out or in the absence of an internet connection.
        """
        data = {
            "trackingReference": tracking_reference,
        }
        return self._api_call(
            service_type=ServiceType.ADMIN_ENABLE_VIRTUAL_ACCOUNT,
            data=data,
            request_reference=request_reference,
        )

    def get_admin_account_balance(
        self, request_reference: Optional[str] = None
    ) -> APIResponse:
        """Retrieves the account balance on your main account.

        Args:
            request_reference: a unique identifier for this api call.
                it is automatically generated if not provided.

        Returns:
            An `APIResponse` which is basically just a dataclass containing the data returned by the server as result
                of calling this function.

        Raises:
            ConnectionException: when the request times out or in the absence of an internet connection.
        """
        return self._api_call(
            service_type=ServiceType.ADMIN_RETRIEVE_MAIN_ACCOUNT_BALANCE,
            request_reference=request_reference,
        )

    def get_virtual_account_balance(
        self, tracking_reference: str, request_reference: Optional[str] = None
    ) -> APIResponse:
        """Retrieves the account balance on your virtual account.

        Args:
            tracking_reference: a unique identifier for the virtual account.
            request_reference: a unique identifier for this api call.
                it is automatically generated if not provided.

        Returns:
            An `APIResponse` which is basically just a dataclass containing the data returned by the server as result
                of calling this function.

        Raises:
            ConnectionException: when the request times out or in the absence of an internet connection.
        """
        data = {
            "trackingReference": tracking_reference,
        }
        return self._api_call(
            service_type=ServiceType.RETRIEVE_VIRTUAL_ACCOUNT_BALANCE,
            data=data,
            request_reference=request_reference,
        )
