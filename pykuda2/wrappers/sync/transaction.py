from typing import Optional

from pykuda2.base import APIWrapper, ServiceType, TransferInstruction


class Transaction(APIWrapper):
    def get_banks(self):
        """Gets all the bank list from NIPS
        Note:
             In production, the list of banks and bank codes may change based o
             n the responses gotten from NIBSS (Nigerian Interbank Settlement System).
        """
        return self.api_call(service_type=ServiceType.BANK_LIST)

    def confirm_transfer_recipient(
        self,
        beneficiary_account_number: str,
        beneficiary_bank_code: str,
        sender_tracking_reference: str,
        is_request_from_virtual_account: bool,
    ):
        """
        Retrieves information of a beneficiary for validation before initiating a transfer.
        """
        data = {
            "beneficiaryAccountNumber": beneficiary_account_number,
            "beneficiaryBankCode": beneficiary_bank_code,
            "SenderTrackingReference": sender_tracking_reference,
            "isRequestFromVirtualAccount": is_request_from_virtual_account,
        }
        return self.api_call(service_type=ServiceType.NAME_ENQUIRY, data=data)

    def fund_transfer(
        self,
        tracking_reference: str,
        beneficiary_account: str,
        beneficiary_bank_code: str,
        beneficiary_name: str,
        amount: int,
        narration: str,
        name_enquiry_session_id: str,
        sender_name: str,
        client_fee_charge: int,
        client_account_number: Optional[str] = None,
    ):
        """
        Sends money from your main Kuda account to another bank accounts.

        Note:
            Please, do not use sensitive data while doing test transactions so
            as not to save it in your sandbox environment.
        """
        data = {
            "ClientAccountNumber": client_account_number,
            "beneficiaryAccount": beneficiary_account,
            "beneficiaryBankCode": beneficiary_bank_code,
            "beneficiaryName": beneficiary_name,
            "amount": amount,
            "narration": narration,
            "nameEnquirySessionID": name_enquiry_session_id,
            "trackingReference": tracking_reference,
            "senderName": sender_name,
            "clientFeeCharge": client_fee_charge,
        }
        return self.api_call(service_type=ServiceType.SINGLE_FUND_TRANSFER, data=data)

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
        client_fee_charge: int,
    ):
        """Transfer money from a virtual account to another and any other Nigerian bank account."""
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
        }
        return self.api_call(
            service_type=ServiceType.VIRTUAL_ACCOUNT_FUND_TRANSFER, data=data
        )

    def process_transfers(
        self,
        fund_transfer_instructions: list[TransferInstruction],
    ):
        data = {
            "FundTransferInstructions": [
                fund_transfer_instruction.to_dict()
                for fund_transfer_instruction in fund_transfer_instructions
            ]
        }
        return self.api_call(
            service_type=ServiceType.FUND_TRANSFER_INSTRUCTION, data=data
        )

    def get_transfer_instructions(
        self,
        account_number: str,
        reference: str,
        amount: int,
        original_request_ref: str,
        status: str,
        page_number: int,
        page_size: int,
    ):
        data = {
            "AccountNumber": account_number,
            "Reference": reference,
            "Amount": amount,
            "OriginalRequestRef": original_request_ref,
            "Status": status,
            "PageNumber": page_number,
            "PageSize": page_size,
        }
        return self.api_call(
            service_type=ServiceType.SEARCH_FUND_TRANSFER_INSTRUCTION, data=data
        )

    def get_transaction_logs(
        self,
        request_reference: str,
        response_reference: str,
        transaction_date: str,
        has_transaction_date_range_filter: str,
        start_date: str,
        end_date: str,
        page_size: str,
        page_number: str,
        fetch_successful_records=False,
    ):
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
        return self.api_call(
            service_type=ServiceType.RETRIEVE_TRANSACTION_LOGS, data=data
        )

    def get_transaction_history(self, page_size: int, page_number: int):
        data = {"pageSize": page_size, "pageNumber": page_number}
        return self.api_call(
            service_type=ServiceType.ADMIN_MAIN_ACCOUNT_TRANSACTIONS, data=data
        )

    def get_filtered_transaction_history(
        self, page_size: int, page_number: int, start_date: str, end_date: str
    ):
        data = {
            "pageSize": page_size,
            "pageNumber": page_number,
            "startDate": start_date,
            "endDate": end_date,
        }
        return self.api_call(
            service_type=ServiceType.ADMIN_MAIN_ACCOUNT_FILTERED_TRANSACTIONS, data=data
        )

    def get_virtual_account_transaction_history(
        self, page_size: int, page_number: int, tracking_reference: str
    ):
        """Retrieves a list of all virtual account transactions"""
        data = {
            "trackingReference": tracking_reference,
            "pageSize": page_size,
            "pageNumber": page_number,
        }
        return self.api_call(
            service_type=ServiceType.ADMIN_VIRTUAL_ACCOUNT_TRANSACTIONS, data=data
        )

    def get_virtual_account_filtered_transaction_history(
        self,
        page_size: str,
        page_number: str,
        start_date: str,
        end_date: str,
        tracking_reference: str,
    ):
        """Retrieves a filtered list of all virtual account transactions"""
        data = {
            "trackingReference": tracking_reference,
            "pageSize": page_size,
            "pageNumber": page_number,
            "startDate": start_date,
            "endDate": end_date,
        }
        return self.api_call(
            service_type=ServiceType.ADMIN_VIRTUAL_ACCOUNT_FILTERED_TRANSACTIONS,
            data=data,
        )

    def get_status(
        self, is_third_party_bank_transfer: bool, transaction_request_reference: str
    ):
        """Retrieves the status of a transaction."""
        data = {
            "isThirdPartyBankTransfer": is_third_party_bank_transfer,
            "transactionRequestReference": transaction_request_reference,
        }
        return self.api_call(
            service_type=ServiceType.TRANSACTION_STATUS_QUERY, data=data
        )

    def fund_virtual_account(
        self, tracking_reference: str, amount: int, narration: str
    ):
        """Add funds to a virtual account"""
        data = {
            "trackingReference": tracking_reference,
            "amount": amount,
            "narration": narration,
        }
        return self.api_call(service_type=ServiceType.FUND_VIRTUAL_ACCOUNT, data=data)

    def withdraw_from_virtual_account(
        self,
        tracking_reference: str,
        amount: int,
        narration: str,
        client_fee_charge: int,
    ):
        """Lets you transfer funds from a virtual account to an associated Kuda
        account or to any other Nigerian Bank account.
        """
        data = {
            "trackingReference": tracking_reference,
            "amount": amount,
            "narration": narration,
            "ClientFeeCharge": client_fee_charge,
        }
        return self.api_call(
            service_type=ServiceType.WITHDRAW_VIRTUAL_ACCOUNT, data=data
        )
