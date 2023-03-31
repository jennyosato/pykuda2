from pykuda2.base import BaseAPIWrapper
from pykuda2.utils import TransactionType, ServiceType


class Savings(BaseAPIWrapper):
    def create_plain_savings_account(self, name: str, tracking_reference: str):
        data = {"Name": name, "TrackingReference": tracking_reference}
        return self.api_call(service_type=ServiceType.CREATE_PLAIN_SAVE, data=data)

    def get_plain_savings_account(
        self, tracking_reference: str, primary_account_number: str
    ):
        data = {
            "TrackingReference": tracking_reference,
            "PrimaryAccountNumber": primary_account_number,
        }
        return self.api_call(service_type=ServiceType.GET_PLAIN_SAVE, data=data)

    def get_plain_savings_accounts(self, primary_account_number: str):
        data = {"PrimaryAccountNumber": primary_account_number}
        return self.api_call(
            service_type=ServiceType.GET_ALL_CUSTOMER_PLAIN_SAVE, data=data
        )

    def credit_or_debit_plain_savings_account(
        self,
        amount: int,
        narration: str,
        transaction_type: TransactionType,
        tracking_reference: str,
    ):
        data = {
            "Amount": amount,
            "Narration": narration,
            "TransactionType": transaction_type,
            "TrackingReference": tracking_reference,
        }
        return self.api_call(
            service_type=ServiceType.PLAIN_SAVE_DEBIT_CREDIT, data=data
        )

    def get_plain_savings_account_transactions(
        self, page_size: int, page_number: int, tracking_reference: str
    ):
        data = {
            "PageSize": page_size,
            "PageNumber": page_number,
            "TrackingReference": tracking_reference,
        }
        return self.api_call(
            service_type=ServiceType.RETRIEVE_PLAIN_SAVE_TRANSACTIONS, data=data
        )

    def create_open_flexible_savings_account(
        self,
        duration: str,
        frequency: str,
        start_now: bool,
        start_date: str,
        savings_tracking_reference: str,
        name: str,
        virtual_account_tracking_reference: str,
        amount: int,
    ):
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
        return self.api_call(
            service_type=ServiceType.CREATE_OPEN_FLEXIBLE_SAVE, data=data
        )

    def pre_create_open_flexible_savings_account(
        self,
        is_interest_earning: bool,
        duration: str,
        frequency: str,
        start_now: bool,
        start_date: str,
        savings_tracking_reference: str,
        name: str,
        virtual_account_tracking_reference: str,
        amount: int,
    ):
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
        return self.api_call(
            service_type=ServiceType.PRE_CREATE_OPEN_FLEXIBLE_SAVE, data=data
        )

    def get_open_flexible_savings_account(
        self, tracking_reference: str, primary_account_number: str
    ):
        data = {
            "TrackingReference": tracking_reference,
            "PrimaryAccountNumber": primary_account_number,
        }
        return self.api_call(service_type=ServiceType.GET_OPEN_FLEXIBLE_SAVE, data=data)

    def get_open_flexible_savings_accounts(self, primary_account_number):
        data = {"PrimaryAccountNumber": primary_account_number}
        return self.api_call(
            service_type=ServiceType.GET_ALL_CUSTOMER_OPEN_FLEXIBLE_SAVE, data=data
        )

    def withdrawal_from_flexible_savings_account(
        self, amount: int, tracking_reference: str
    ):
        data = {"Amount": amount, "TrackingReference": tracking_reference}
        return self.api_call(
            service_type=ServiceType.COMPLETE_OPEN_FLEXIBLE_SAVE_WITHDRAWAL, data=data
        )

    def get_flexible_savings_account_transactions(
        self, page_size: int, page_number: int, tracking_reference: str
    ):
        data = {
            "PageSize": page_size,
            "PageNumber": page_number,
            "TrackingReference": tracking_reference,
        }
        return self.api_call(
            service_type=ServiceType.RETRIEVE_OPEN_FLEXIBLE_SAVE_TRANSACTIONS, data=data
        )

    def create_fixed_savings_account(
        self,
        is_interest_earning: bool,
        duration: str,
        frequency: str,
        start_now: bool,
        start_date: str,
        savings_tracking_reference: str,
        name: str,
        virtual_account_tracking_reference: str,
        amount: int,
    ):
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
        return self.api_call(service_type=ServiceType.CREATE_FIXED_SAVE, data=data)

    def get_fixed_savings_account(
        self, tracking_reference: str, primary_account_number: str
    ):
        data = {
            "TrackingReference": tracking_reference,
            "PrimaryAccountNumber": primary_account_number,
        }
        return self.api_call(service_type=ServiceType.GET_FIXED_SAVE, data=data)

    def get_fixed_savings_accounts(self, primary_account_number):
        data = {"PrimaryAccountNumber": primary_account_number}
        return self.api_call(
            service_type=ServiceType.GET_ALL_CUSTOMER_FIXED_SAVE, data=data
        )

    def close_fixed_savings_account(self, amount: int, tracking_reference: str):
        data = {"Amount": amount, "TrackingReference": tracking_reference}
        return self.api_call(
            service_type=ServiceType.COMPLETE_FIXED_SAVE_WITHDRAWAL, data=data
        )

    def get_fixed_savings_account_transactions(
        self, page_number: int, page_size: int, tracking_reference: str
    ):
        data = {
            "PageNumber": page_number,
            "PageSize": page_size,
            "TrackingReference": tracking_reference,
        }
        return self.api_call(
            service_type=ServiceType.RETRIEVE_FIXED_SAVE_TRANSACTIONS, data=data
        )
