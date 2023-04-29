from typing import Optional

from pykuda2.base import BaseAPIWrapper
from pykuda2.utils import TransactionType, ServiceType, APIResponse


class Savings(BaseAPIWrapper):
    def create_plain_savings_account(
        self,
        name: str,
        tracking_reference: str,
        request_reference: Optional[str] = None,
    ) -> APIResponse:
        """Create a Plain Savings Account.

        To create a Plain savings, in your request, you need to state the Virtual Account
        associated with this savings account as well as create a unique identifier for
        the savings account to be created.

        Args:
            name: The savings plan name.
            tracking_reference: The virtual account transaction reference number.
            request_reference: a unique identifier for this api call.
                it is automatically generated if not provided.

        Returns:
            An `APIResponse` which is basically just a dataclass containing the data returned by the server as result
                of calling this function.

        Raises:
            ConnectionException: when the request times out or in the absence of an internet connection.
        """
        data = {"Name": name, "TrackingReference": tracking_reference}
        return self._api_call(
            service_type=ServiceType.CREATE_PLAIN_SAVE,
            data=data,
            request_reference=request_reference,
        )

    def get_plain_savings_account(
        self,
        tracking_reference: str,
        primary_account_number: str,
        request_reference: Optional[str] = None,
    ) -> APIResponse:
        """Retrieves a customers plain savings account

        Args:
            tracking_reference: Account transaction reference number of the savings you want to retrieve.
                This parameter is for specific plain savings.
            primary_account_number: Account number of the specific customer.
            request_reference: a unique identifier for this api call.
                it is automatically generated if not provided.

        Returns:
            An `APIResponse` which is basically just a dataclass containing the data returned by the server as result
                of calling this function.

        Raises:
            ConnectionException: when the request times out or in the absence of an internet connection.
        """
        data = {
            "TrackingReference": tracking_reference,
            "PrimaryAccountNumber": primary_account_number,
        }
        return self._api_call(service_type=ServiceType.GET_PLAIN_SAVE, data=data)

    def get_plain_savings_accounts(
        self, tracking_reference: str, request_reference: Optional[str] = None
    ) -> APIResponse:
        """Retrieves all customers plain savings accounts

        Args:
            tracking_reference: Account transaction reference number of the savings you want to retrieve.
                This parameter is for specific plain savings.
            request_reference: a unique identifier for this api call.
                it is automatically generated if not provided.

        Returns:
            An `APIResponse` which is basically just a dataclass containing the data returned by the server as result
                of calling this function.

        Raises:
            ConnectionException: when the request times out or in the absence of an internet connection.
        """
        data = {"TrackingReference": tracking_reference}
        return self._api_call(
            service_type=ServiceType.GET_ALL_CUSTOMER_PLAIN_SAVE,
            data=data,
            request_reference=request_reference,
        )

    def credit_or_debit_plain_savings_account(
        self,
        amount: int,
        narration: str,
        transaction_type: TransactionType,
        tracking_reference: str,
        request_reference: Optional[str] = None,
    ) -> APIResponse:
        """Adds or removes money from a plain savings account.

        Args:
            amount: The amount to be added or removed.
            narration: The transaction description.
            transaction_type: The transaction type e.g. TransactionType.CREDIT.
            tracking_reference: Unique identifier for savings.
            request_reference: a unique identifier for this api call.
                it is automatically generated if not provided.

        Returns:
            An `APIResponse` which is basically just a dataclass containing the data returned by the server as result
                of calling this function.

        Raises:
            ConnectionException: when the request times out or in the absence of an internet connection.
        """
        data = {
            "Amount": amount,
            "Narration": narration,
            "TransactionType": transaction_type,
            "TrackingReference": tracking_reference,
        }
        return self._api_call(
            service_type=ServiceType.PLAIN_SAVE_DEBIT_CREDIT,
            data=data,
            request_reference=request_reference,
        )

    def get_plain_savings_account_transactions(
        self,
        page_size: int,
        page_number: int,
        tracking_reference: str,
        request_reference: Optional[str] = None,
    ) -> APIResponse:
        """Retrieves all plain savings account transaction data.

        Args:
            tracking_reference: Unique identifier for account.
            page_size: This specifies the number of transactions to be retrieved.
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
            "TrackingReference": tracking_reference,
        }
        return self._api_call(
            service_type=ServiceType.RETRIEVE_PLAIN_SAVE_TRANSACTIONS,
            data=data,
            request_reference=request_reference,
        )

    def create_open_flexible_savings_account(
        self,
        savings_tracking_reference: str,
        name: str,
        virtual_account_tracking_reference: str,
        amount: int,
        duration: str,
        frequency: str,
        start_now: bool,
        start_date: Optional[str],
        request_reference: Optional[str] = None,
    ) -> APIResponse:
        """Create an open savings plan.

        Args:
            savings_tracking_reference: The unique identifier for savings.
            name: Name of the savings plan.
            virtual_account_tracking_reference: Unique identifier for the associated virtual account.
            amount: Amount to be saved.
            duration: Length of savings.
            frequency: How often the savings should happen.
            start_now: Flag to start the savings immediately.
            start_date: Starting date of the savings. Required if `start_now` is `False`.
                Format (YYYY-MM-DD).
            request_reference: a unique identifier for this api call.
                it is automatically generated if not provided.

        Returns:
            An `APIResponse` which is basically just a dataclass containing the data returned by the server as result
                of calling this function.

        Raises:
            ConnectionException: when the request times out or in the absence of an internet connection.
        """
        data = {
            "SavingsTrackingReference": savings_tracking_reference,
            "Name": name,
            "VirtualAccountTrackingReference": virtual_account_tracking_reference,
            "Amount": amount,
            "Duration": duration,
            "Frequency": frequency,
            "StartNow": start_now,
            "StartData": start_date,
        }
        return self._api_call(
            service_type=ServiceType.CREATE_OPEN_FLEXIBLE_SAVE,
            data=data,
            request_reference=request_reference,
        )

    def pre_create_open_flexible_savings_account(
        self,
        savings_tracking_reference: str,
        name: str,
        virtual_account_tracking_reference: str,
        amount: int,
        duration: str,
        frequency: str,
        start_now: bool,
        start_date: str,
        is_interest_earning: bool,
        request_reference: Optional[str] = None,
    ) -> APIResponse:
        """Pre create an Open Flexible Savings account.

        Args:
            savings_tracking_reference: The unique identifier for savings.
            name: Name of the savings plan.
            virtual_account_tracking_reference: Unique identifier for the associated virtual account.
            amount: Amount to be saved.
            duration: Length of savings.
            frequency: How often the savings should happen.
            start_now: Flag to start the savings immediately.
            start_date: Starting date of the savings. Required if `start_now` is `False`.
                Format (YYYY-MM-DD).
            is_interest_earning: Will the savings earn interest or not.
            request_reference: a unique identifier for this api call.
                it is automatically generated if not provided.

        Returns:
            An `APIResponse` which is basically just a dataclass containing the data returned by the server as result
                of calling this function.

        Raises:
            ConnectionException: when the request times out or in the absence of an internet connection.
        """
        data = {
            "SavingsTrackingReference": savings_tracking_reference,
            "Name": name,
            "VirtualAccountTrackingReference": virtual_account_tracking_reference,
            "Amount": amount,
            "Duration": duration,
            "Frequency": frequency,
            "StartNow": start_now,
            "StartData": start_date,
            "IsInterestEarning": is_interest_earning,
        }
        return self._api_call(
            service_type=ServiceType.PRE_CREATE_OPEN_FLEXIBLE_SAVE,
            data=data,
            request_reference=request_reference,
        )

    def get_open_flexible_savings_account(
        self,
        tracking_reference: str,
        primary_account_number: str,
        request_reference: Optional[str] = None,
    ) -> APIResponse:
        """Retrieve an open flexible savings account.

        Args:
            tracking_reference: Account transaction reference number of the savings you want to retrieve.
            primary_account_number: Account number of the specific customer.
            request_reference: a unique identifier for this api call.
                it is automatically generated if not provided.

        Returns:
            An `APIResponse` which is basically just a dataclass containing the data returned by the server as result
                of calling this function.

        Raises:
            ConnectionException: when the request times out or in the absence of an internet connection.
        """
        data = {
            "TrackingReference": tracking_reference,
            "PrimaryAccountNumber": primary_account_number,
        }
        return self._api_call(
            service_type=ServiceType.GET_OPEN_FLEXIBLE_SAVE,
            data=data,
            request_reference=request_reference,
        )

    def get_open_flexible_savings_accounts(
        self,
        tracking_reference: str,
        primary_account_number: str,
        request_reference: Optional[str] = None,
    ) -> APIResponse:
        """Retrieves all flexible savings account.

        Args:
            tracking_reference: Account transaction reference number of the savings you want to retrieve.
            primary_account_number: Account number of the specific customer.
            request_reference: a unique identifier for this api call.
                it is automatically generated if not provided.

        Returns:
            An `APIResponse` which is basically just a dataclass containing the data returned by the server as result
                of calling this function.

        Raises:
            ConnectionException: when the request times out or in the absence of an internet connection.
        """
        data = {
            "TrackingReference": tracking_reference,
            "PrimaryAccountNumber": primary_account_number,
        }
        return self._api_call(
            service_type=ServiceType.GET_ALL_CUSTOMER_OPEN_FLEXIBLE_SAVE,
            data=data,
            request_reference=request_reference,
        )

    def withdrawal_from_flexible_savings_account(
        self,
        amount: int,
        tracking_reference: str,
        request_reference: Optional[str] = None,
    ) -> APIResponse:
        """

        Args:
            amount: Amount to be removed.
            tracking_reference: Unique identifier for savings.
            request_reference: a unique identifier for this api call.
                it is automatically generated if not provided.

        Returns:
            An `APIResponse` which is basically just a dataclass containing the data returned by the server as result
                of calling this function.

        Raises:
            ConnectionException: when the request times out or in the absence of an internet connection.
        """
        data = {"Amount": amount, "TrackingReference": tracking_reference}
        return self._api_call(
            service_type=ServiceType.COMPLETE_OPEN_FLEXIBLE_SAVE_WITHDRAWAL,
            data=data,
            request_reference=request_reference,
        )

    def get_flexible_savings_account_transactions(
        self,
        tracking_reference: str,
        page_size: int,
        page_number: int,
        request_reference: Optional[str] = None,
    ) -> APIResponse:
        """

        Args:
            tracking_reference: Account tracking reference number.
            page_size: This specifies the number of transactions to be retrieved.
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
            "TrackingReference": tracking_reference,
        }
        return self._api_call(
            service_type=ServiceType.RETRIEVE_OPEN_FLEXIBLE_SAVE_TRANSACTIONS,
            data=data,
            request_reference=request_reference,
        )

    def create_fixed_savings_account(
        self,
        savings_tracking_reference: str,
        name: str,
        virtual_account_tracking_reference: str,
        amount: int,
        duration: str,
        frequency: str,
        start_now: bool,
        start_date: str,
        is_interest_earning: bool,
        request_reference: Optional[str] = None,
    ) -> APIResponse:
        """Creates a fixed account.

        Args:
            savings_tracking_reference: The unique identifier for savings.
            name: Name of the savings plan.
            virtual_account_tracking_reference: Unique identifier for the associated virtual account.
            amount: Amount to be saved.
            duration: Length of savings.
            frequency: How often the savings should happen.
            start_now: Flag to start the savings immediately.
            start_date: Starting date of the savings. Required if `start_now` is `False`.
                Format (YYYY-MM-DD).
            is_interest_earning: Will the savings earn interest or not.
            request_reference: a unique identifier for this api call.
                it is automatically generated if not provided.

        Returns:
            An `APIResponse` which is basically just a dataclass containing the data returned by the server as result
                of calling this function.

        Raises:
            ConnectionException: when the request times out or in the absence of an internet connection.
        """
        data = {
            "SavingsTrackingReference": savings_tracking_reference,
            "Name": name,
            "VirtualAccountTrackingReference": virtual_account_tracking_reference,
            "Amount": amount,
            "Duration": duration,
            "Frequency": frequency,
            "StartNow": start_now,
            "StartData": start_date,
            "IsInterestEarning": is_interest_earning,
        }
        return self._api_call(
            service_type=ServiceType.CREATE_FIXED_SAVE,
            data=data,
            request_reference=request_reference,
        )

    def get_fixed_savings_account(
        self,
        tracking_reference: str,
        request_reference: Optional[str] = None,
    ) -> APIResponse:
        """Retrieves a fixed savings account.

        Args:
            tracking_reference: Account transaction reference number of the savings you want to retrieve.
            request_reference: a unique identifier for this api call.
                it is automatically generated if not provided.

        Returns:
            An `APIResponse` which is basically just a dataclass containing the data returned by the server as result
                of calling this function.

        Raises:
            ConnectionException: when the request times out or in the absence of an internet connection.
        """
        data = {
            "SavingsId": tracking_reference,
        }
        return self._api_call(
            service_type=ServiceType.GET_FIXED_SAVE,
            data=data,
            request_reference=request_reference,
        )

    def get_fixed_savings_accounts(
        self, tracking_reference: str, request_reference: Optional[str] = None
    ) -> APIResponse:
        """Retrieves all fixed savings you want to retrieve.

        Args:
            tracking_reference: Account transaction reference number of the savings you want to retrieve.
            request_reference: a unique identifier for this api call.
                it is automatically generated if not provided.

        Returns:
            An `APIResponse` which is basically just a dataclass containing the data returned by the server as result
                of calling this function.

        Raises:
            ConnectionException: when the request times out or in the absence of an internet connection.
        """
        data = {"TrackingReference": tracking_reference}
        return self._api_call(
            service_type=ServiceType.GET_ALL_CUSTOMER_FIXED_SAVE,
            data=data,
            request_reference=request_reference,
        )

    def close_fixed_savings_account(
        self,
        amount: int,
        tracking_reference: str,
        request_reference: Optional[str] = None,
    ) -> APIResponse:
        """

        Args:
            amount: amount to be removed.
            tracking_reference: unique identifier for the savings.
            request_reference: a unique identifier for this api call.
                it is automatically generated if not provided.

        Returns:
            An `APIResponse` which is basically just a dataclass containing the data returned by the server as result
                of calling this function.

        Raises:
            ConnectionException: when the request times out or in the absence of an internet connection.
        """
        data = {"Amount": amount, "SavingsId": tracking_reference}
        return self._api_call(
            service_type=ServiceType.COMPLETE_FIXED_SAVE_WITHDRAWAL,
            data=data,
            request_reference=request_reference,
        )

    def get_fixed_savings_account_transactions(
        self,
        tracking_reference: str,
        page_number: int,
        page_size: int,
        request_reference: Optional[str] = None,
    ) -> APIResponse:
        """Retrieves all fixed savings account transaction

        Args:
            tracking_reference: Account tracking reference number.
            page_size: This specifies the number of transactions to be retrieved.
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
            "PageNumber": page_number,
            "PageSize": page_size,
            "SavingsId": tracking_reference,
        }
        return self._api_call(
            service_type=ServiceType.RETRIEVE_FIXED_SAVE_TRANSACTIONS,
            data=data,
            request_reference=request_reference,
        )
