from typing import Optional

from pykuda2.base import BaseAPIWrapper
from pykuda2.utils import (
    TransferInstruction,
    ServiceType,
    TransactionStatus,
    APIResponse,
)


class Transaction(BaseAPIWrapper):
    def get_banks(self, request_reference: Optional[str] = None) -> APIResponse:
        """Retrieves all the banks available from NIPS

         In production, the list of banks and bank codes may change based on
         the responses gotten from NIBSS (Nigerian Interbank Settlement System).

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
            service_type=ServiceType.BANK_LIST, request_reference=request_reference
        )

    def confirm_transfer_recipient(
        self,
        beneficiary_account_number: str,
        beneficiary_bank_code: str,
        sender_tracking_reference: Optional[str],
        is_request_from_virtual_account: bool,
        request_reference: Optional[str] = None,
    ) -> APIResponse:
        """
        Retrieves information of a beneficiary for validation before initiating a transfer.

        Args:
            beneficiary_account_number: Destination bank account number.
            beneficiary_bank_code: Destination bank code.
            sender_tracking_reference: Tracking reference of the virtual account trying to
                do the actual transfer. Leave it empty if the intended transfer is going to
                be from the main account.
            is_request_from_virtual_account: If the intended transfer is to be made by the
                virtual account.
            request_reference: a unique identifier for this api call.
                it is automatically generated if not provided.

        Returns:
            An `APIResponse` which is basically just a dataclass containing the data returned by the server as result
                of calling this function.

        Raises:
            ConnectionException: when the request times out or in the absence of an internet connection.
        """
        data = {
            "beneficiaryAccountNumber": beneficiary_account_number,
            "beneficiaryBankCode": beneficiary_bank_code,
            "SenderTrackingReference": sender_tracking_reference,
            "isRequestFromVirtualAccount": is_request_from_virtual_account,
        }
        return self._api_call(
            service_type=ServiceType.NAME_ENQUIRY,
            data=data,
            request_reference=request_reference,
        )

    def fund_transfer(
        self,
        beneficiary_account: str,
        beneficiary_bank_code: str,
        beneficiary_name: str,
        amount: int,
        narration: str,
        name_enquiry_session_id: str,
        sender_name: str,
        client_fee_charge: int = 0,
        client_account_number: Optional[str] = None,
        request_reference: Optional[str] = None,
    ) -> APIResponse:
        """
        Sends money from your main Kuda account to another bank accounts.

        Please, do not use sensitive data while doing test transactions so
        as not to save it in your sandbox environment.

        Args:
            beneficiary_account: Destination bank account number.
            beneficiary_bank_code: Destination bank code.
            beneficiary_name: Name of the recipient.
            amount: Amount to be transferred.
            narration: User defined reason for the transaction.
            name_enquiry_session_id: Session ID generated from the nameEnquiry request.
            sender_name: Name of the person sending money.
            client_fee_charge: It is an amount a client wishes to charge their customer
                for a transfer being carried out.
            client_account_number: Account number of the client where the charged fee is
                sent to.
            request_reference: a unique identifier for this api call.
                it is automatically generated if not provided.

        Returns:
            An `APIResponse` which is basically just a dataclass containing the data returned by the server as result
                of calling this function.

        Raises:
            ConnectionException: when the request times out or in the absence of an internet connection.
        """
        data = {
            "ClientAccountNumber": client_account_number,
            "beneficiaryAccount": beneficiary_account,
            "beneficiaryBankCode": beneficiary_bank_code,
            "beneficiaryName": beneficiary_name,
            "amount": amount,
            "narration": narration,
            "nameEnquirySessionID": name_enquiry_session_id,
            "senderName": sender_name,
            "clientFeeCharge": client_fee_charge,
        }
        return self._api_call(
            service_type=ServiceType.SINGLE_FUND_TRANSFER,
            data=data,
            request_reference=request_reference,
        )

    def virtual_account_fund_transfer(
        self,
        tracking_reference: str,
        beneficiary_account: str,
        amount: int,
        beneficiary_name: str,
        narration: str,
        beneficiary_bank_code: str,
        sender_name: str,
        name_enquiry_id: str,
        client_fee_charge: int = 0,
        client_account_number: Optional[str] = None,
        request_reference: Optional[str] = None,
    ) -> APIResponse:
        """Transfer money from a virtual account to another and any other Nigerian bank account.

        Args:
            tracking_reference: Unique identifier of the sender.
            beneficiary_account: Destination bank account number.
            beneficiary_bank_code: Destination bank code.
            beneficiary_name: Name of the recipient.
            amount: Amount to be transferred.
            narration: User defined reason for the transaction.
            name_enquiry_id: Session ID generated from the nameEnquiry request.
            sender_name: Name of the person sending money.
            client_fee_charge: It is an amount a client wishes to charge their customer
                for a transfer being carried out.
            client_account_number: Account number of the client where the charged fee is
                sent to.
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
            "beneficiaryAccount": beneficiary_account,
            "amount": amount,
            "narration": narration,
            "beneficiaryBankCode": beneficiary_bank_code,
            "beneficiaryName": beneficiary_name,
            "senderName": sender_name,
            "nameEnquiryId": name_enquiry_id,
            "clientFeeCharge": client_fee_charge,
            "ClientAccountNumber": client_account_number,
        }
        return self._api_call(
            service_type=ServiceType.VIRTUAL_ACCOUNT_FUND_TRANSFER,
            data=data,
            request_reference=request_reference,
        )

    def process_transfers(
        self,
        fund_transfer_instructions: list[TransferInstruction],
        request_reference: Optional[str] = None,
    ) -> APIResponse:
        """Allows you to send a list of transfer instructions to Kuda, to make the payments on your behalf.

        Args:
            fund_transfer_instructions: A list of transfer instructions for transfers to be made.
            request_reference: a unique identifier for this api call.
                it is automatically generated if not provided.

        Returns:
            An `APIResponse` which is basically just a dataclass containing the data returned by the server as result
                of calling this function.

        Raises:
            ConnectionException: when the request times out or in the absence of an internet connection.
        """
        data = {
            "FundTransferInstructions": [
                fund_transfer_instruction.to_dict()
                for fund_transfer_instruction in fund_transfer_instructions
            ]
        }
        return self._api_call(
            service_type=ServiceType.FUND_TRANSFER_INSTRUCTION,
            data=data,
            request_reference=request_reference,
        )

    def get_transfer_instructions(
        self,
        account_number: str,
        reference: str,
        amount: int,
        original_request_ref: str,
        status: TransactionStatus,
        page_number: int,
        page_size: int,
        request_reference: Optional[str] = None,
    ) -> APIResponse:
        """Retrieves transfer instructions and returns the status of the transaction.

        Args:
            account_number: The beneficiary’s account number.
            reference: The reference on the transfer instruction.
            amount: The transaction amount.
            original_request_ref: The request reference used in logging the instruction.
            status: The status of the transaction.
            page_size: This specifies the number of transfer instructions to be retrieved.
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
            "AccountNumber": account_number,
            "Reference": reference,
            "Amount": amount,
            "OriginalRequestRef": original_request_ref,
            "Status": status,
            "PageNumber": page_number,
            "PageSize": page_size,
        }
        return self._api_call(
            service_type=ServiceType.SEARCH_FUND_TRANSFER_INSTRUCTION,
            data=data,
            request_reference=request_reference,
        )

    def get_transaction_logs(
        self,
        request_reference: str,
        response_reference: str,
        transaction_date: str,
        has_transaction_date_range_filter: bool,
        start_date: str,
        end_date: str,
        page_size: int,
        page_number: int,
        fetch_successful_records: bool=False,
    ) -> APIResponse:
        """Retrieves all transactions.

        Args:
            request_reference: a unique identifier for this api call.
                it is automatically generated if not provided.
            response_reference: Transaction response reference.
            fetch_successful_records: If set to `True`, only successful transactions
                will be retrieved.
            transaction_date: The transaction date. Format (YYYY-MM-DD)
            has_transaction_date_range_filter: Is set to `True`, then the `start_date` and
                `end_date` parameter will be used instead of `transaction_date`
            start_date: Transaction start date. Format (YYYY-MM-DD)
            end_date: Transaction end date. Format (YYYY-MM-DD)
            page_size: This specifies the number of transactions to be retrieved.
            page_number: This specifies the index of the paginated results retrieved.

        Returns:
            An `APIResponse` which is basically just a dataclass containing the data returned by the server as result
                of calling this function.

        Raises:
            ConnectionException: when the request times out or in the absence of an internet connection.
        """
        data = {
            "RequestReference": request_reference,
            "ResponseReference": response_reference,
            "FetchSuccessfulRecords": fetch_successful_records,
            "TransactionDate": transaction_date,
            "HasTransactionDateRangeFilter": has_transaction_date_range_filter,
            "StartDate": start_date,
            "EndDate": end_date,
            "PageSize": page_size,
            "PageNumber": page_number,
        }
        return self._api_call(
            service_type=ServiceType.RETRIEVE_TRANSACTION_LOGS,
            data=data,
            request_reference=request_reference,
        )

    def get_transaction_history(
        self, page_size: int, page_number: int, request_reference: Optional[str] = None
    ) -> APIResponse:
        """Retrieves a list of all main account transactions.

        Args:
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
        data = {"pageSize": page_size, "pageNumber": page_number}
        return self._api_call(
            service_type=ServiceType.ADMIN_MAIN_ACCOUNT_TRANSACTIONS,
            data=data,
            request_reference=request_reference,
        )

    def get_filtered_transaction_history(
        self,
        page_size: int,
        page_number: int,
        start_date: str,
        end_date: str,
        request_reference: Optional[str] = None,
    ) -> APIResponse:
        """Retrieves a filtered transaction history.

        Args:
            start_date: Transaction start date. Format (YYYY-MM-DD)
            end_date: Transaction end date. Format (YYYY-MM-DD)
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
            "pageSize": page_size,
            "pageNumber": page_number,
            "startDate": start_date,
            "endDate": end_date,
        }
        return self._api_call(
            service_type=ServiceType.ADMIN_MAIN_ACCOUNT_FILTERED_TRANSACTIONS,
            data=data,
            request_reference=request_reference,
        )

    def get_virtual_account_transaction_history(
        self,
        tracking_reference: str,
        page_size: int,
        page_number: int,
        request_reference: Optional[str] = None,
    ) -> APIResponse:
        """Retrieves a list of all virtual account transactions.

        Args:
            tracking_reference: The virtual account unique identifier.
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
            "trackingReference": tracking_reference,
            "pageSize": page_size,
            "pageNumber": page_number,
        }
        return self._api_call(
            service_type=ServiceType.ADMIN_VIRTUAL_ACCOUNT_TRANSACTIONS,
            data=data,
            request_reference=request_reference,
        )

    def get_virtual_account_filtered_transaction_history(
        self,
        tracking_reference: str,
        page_size: int,
        page_number: int,
        start_date: str,
        end_date: str,
        request_reference: Optional[str] = None,
    ) -> APIResponse:
        """Retrieves a filtered list of all virtual account transactions.

        Args:
            tracking_reference: The virtual account unique identifier.
            page_size: This specifies the number of transactions to be retrieved.
            page_number: This specifies the index of the paginated results retrieved.
            start_date: Transaction start date. Format (YYYY-MM-DD)
            end_date: Transaction end date. Format (YYYY-MM-DD)
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
            "pageSize": page_size,
            "pageNumber": page_number,
            "startDate": start_date,
            "endDate": end_date,
        }
        return self._api_call(
            service_type=ServiceType.ADMIN_VIRTUAL_ACCOUNT_FILTERED_TRANSACTIONS,
            data=data,
            request_reference=request_reference,
        )

    def get_status(
        self,
        is_third_party_bank_transfer: bool,
        transaction_request_reference: str,
        request_reference: Optional[str] = None,
    ) -> APIResponse:
        """Retrieves the status of a transaction.

        Args:
            is_third_party_bank_transfer: Flag to determine if the transaction was interbank or
                intra-bank.
            transaction_request_reference: The request reference used when make transaction.
            request_reference: a unique identifier for this api call.
                it is automatically generated if not provided.

        Returns:
            An `APIResponse` which is basically just a dataclass containing the data returned by the server as result
                of calling this function.

        Raises:
            ConnectionException: when the request times out or in the absence of an internet connection.
        """
        data = {
            "isThirdPartyBankTransfer": is_third_party_bank_transfer,
            "transactionRequestReference": transaction_request_reference,
        }
        return self._api_call(
            service_type=ServiceType.TRANSACTION_STATUS_QUERY,
            data=data,
            request_reference=request_reference,
        )

    def fund_virtual_account(
        self,
        tracking_reference: str,
        amount: int,
        narration: str,
        request_reference: Optional[str] = None,
    ) -> APIResponse:
        """Add funds to a virtual account.

        Args:
            tracking_reference: The virtual account tracking reference.
            amount: The amount you want to fund your account.
            narration: The additional description for the transaction.
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
            "amount": amount,
            "narration": narration,
        }
        return self._api_call(
            service_type=ServiceType.FUND_VIRTUAL_ACCOUNT,
            data=data,
            request_reference=request_reference,
        )

    def withdraw_from_virtual_account(
        self,
        tracking_reference: str,
        amount: int,
        narration: str,
        client_fee_charge: int = 0,
        request_reference: Optional[str] = None,
    ) -> APIResponse:
        """Transfer funds from a virtual account to an associated Kuda account or to any other Nigerian Bank account.

        Args:
            tracking_reference: The virtual account tracking reference.
            amount: The amount you want to fund your account.
            narration: The additional description for the transaction.
            client_fee_charge: It is an amount a client wishes to charge their customer for a transfer
                being carried out.
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
            "amount": amount,
            "narration": narration,
            "ClientFeeCharge": client_fee_charge,
        }
        return self._api_call(
            service_type=ServiceType.WITHDRAW_VIRTUAL_ACCOUNT,
            data=data,
            request_reference=request_reference,
        )
