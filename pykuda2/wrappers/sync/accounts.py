from typing import Optional

from pykuda2.base import BaseAPIWrapper
from pykuda2.utils import ServiceType


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
    ):
        """Creates a new virtual account for customers.

        Args:
            email: customer's email address.
            phone_number: customer's phone number.
            last_name: customer's last name.
            first_name: customer's first name.
            middle_name: customer's middle name.
            business_name: customer's business name.
            tracking_reference: a unique identifier for the account to be created.

        Returns:
            An `APIResponse` which is basically just a dataclass containing the data returned
            by the server as result of calling this function.

        Raises:
            UnsupportedHTTPMethodException: when and invalid HTTP verb is provided.
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
        return self.api_call(
            service_type=ServiceType.ADMIN_CREATE_VIRTUAL_ACCOUNT, data=data
        )

    def update_virtual_account(
        self,
        tracking_reference: str,
        first_name: Optional[str] = None,
        last_name: Optional[str] = None,
        email: Optional[str] = None,
    ):
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

        Returns:
            An `APIResponse` which is basically just a dataclass containing the data returned
            by the server as result of calling this function.

        Raises:
            UnsupportedHTTPMethodException: when and invalid HTTP verb is provided.
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
        return self.api_call(
            service_type=ServiceType.ADMIN_UPDATE_VIRTUAL_ACCOUNT, data=data
        )

    def get_virtual_accounts(self, page_size: int, page_number: int):
        """Retrieves your existing virtual accounts.

        Args:
            page_size: This specifies the number of virtual accounts to be retrieved.
            page_number: This specifies the index of the paginated results retrieved.

        Returns:
            An `APIResponse` which is basically just a dataclass containing the data returned
            by the server as result of calling this function.

        Raises:
            UnsupportedHTTPMethodException: when and invalid HTTP verb is provided.
            ConnectionException: when the request times out or in the absence of an internet connection.
        """
        data = {
            "PageSize": page_size,
            "PageNumber": page_number,
        }
        return self.api_call(service_type=ServiceType.ADMIN_VIRTUAL_ACCOUNTS, data=data)

    def get_virtual_account(self, tracking_reference: str):
        """Retrieves an existing virtual account.

        Args:
            tracking_reference: the unique identifier tied to the account to be retrieved.

        Returns:
            An `APIResponse` which is basically just a dataclass containing the data returned
            by the server as result of calling this function.

        Raises:
            UnsupportedHTTPMethodException: when and invalid HTTP verb is provided.
            ConnectionException: when the request times out or in the absence of an internet connection.
        """
        data = {
            "trackingReference": tracking_reference,
        }
        return self.api_call(
            service_type=ServiceType.ADMIN_RETRIEVE_SINGLE_VIRTUAL_ACCOUNT, data=data
        )

    def disable_virtual_account(self, tracking_reference: str):
        """Disables a user’s virtual static account.

        Kuda encourages Admins and account managers to review accounts and transactions
        frequently. This will avoid situations where a user has an over bloated customer
        database without real customers or helping to reduce the menace of fraudulent transactions.

        Args:
            tracking_reference: the unique identifier tied to the account to be disabled.

        Returns:
            An `APIResponse` which is basically just a dataclass containing the data returned
            by the server as result of calling this function.

        Raises:
            UnsupportedHTTPMethodException: when and invalid HTTP verb is provided.
            ConnectionException: when the request times out or in the absence of an internet connection.
        """
        data = {
            "trackingReference": tracking_reference,
        }
        return self.api_call(
            service_type=ServiceType.ADMIN_DISABLE_VIRTUAL_ACCOUNT, data=data
        )

    def enable_virtual_account(self, tracking_reference: str):
        """Enables a user’s virtual static account.

        Args:
            tracking_reference: the unique identifier tied to the account to be enabled.

        Returns:
            An `APIResponse` which is basically just a dataclass containing the data returned
            by the server as result of calling this function.

        Raises:
            UnsupportedHTTPMethodException: when and invalid HTTP verb is provided.
            ConnectionException: when the request times out or in the absence of an internet connection.
        """
        data = {
            "trackingReference": tracking_reference,
        }
        return self.api_call(
            service_type=ServiceType.ADMIN_ENABLE_VIRTUAL_ACCOUNT, data=data
        )

    def get_admin_account_balance(self):
        """Retrieves the account balance on your main account.

        Returns:
            An `APIResponse` which is basically just a dataclass containing the data returned
            by the server as result of calling this function.

        Raises:
            UnsupportedHTTPMethodException: when and invalid HTTP verb is provided.
            ConnectionException: when the request times out or in the absence of an internet connection.
        """
        return self.api_call(
            service_type=ServiceType.ADMIN_RETRIEVE_MAIN_ACCOUNT_BALANCE
        )

    def get_virtual_account_balance(self, tracking_reference: str):
        """Retrieves the account balance on your virtual account.

        Returns:
            An `APIResponse` which is basically just a dataclass containing the data returned
            by the server as result of calling this function.

        Raises:
            UnsupportedHTTPMethodException: when and invalid HTTP verb is provided.
            ConnectionException: when the request times out or in the absence of an internet connection.
        """
        data = {
            "trackingReference": tracking_reference,
        }
        return self.api_call(
            service_type=ServiceType.ADMIN_ENABLE_VIRTUAL_ACCOUNT, data=data
        )
