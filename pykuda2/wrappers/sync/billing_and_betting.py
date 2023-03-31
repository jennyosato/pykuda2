from pykuda2.base import APIWrapper
from pykuda2.utils import BillType, ServiceType


class BillingAndBetting(APIWrapper):
    def get_bill_type(self, bill_type: BillType):
        data = {"BillTypeName": bill_type}
        return self.api_call(service_type=ServiceType.GET_BILLERS_BY_TYPE, data=data)

    def verify_customer_before_purchase(
        self,
        tracking_reference: str,
        kuda_bill_item_identifier: str,
        customer_identification: str,
    ):
        data = {
            "TrackingRef": tracking_reference,
            "KudaBillItemIdentifier": kuda_bill_item_identifier,
            "CustomerIdentification": customer_identification,
        }
        return self.api_call(service_type=ServiceType.VERIFY_BILL_CUSTOMER, data=data)

    def purchase_bill(
        self,
        amount: int,
        bill_item_identifier: str,
        phone_number: str,
        customer_identifier: str,
    ):
        """Purchase a bill from your main account"""
        data = {
            "Amount": amount,
            "BillItemIdentifier": bill_item_identifier,
            "PhoneNumber": phone_number,
            "CustomerIdentifier": customer_identifier,
        }
        return self.api_call(service_type=ServiceType.ADMIN_PURCHASE_BILL, data=data)

    def purchase_bill_from_virtual_account(
        self,
        tracking_reference: str,
        amount: int,
        bill_item_identifier: str,
        phone_number: str,
        customer_identifier: str,
    ):
        data = {
            "Amount": amount,
            "BillItemIdentifier": bill_item_identifier,
            "PhoneNumber": phone_number,
            "CustomerIdentifier": customer_identifier,
            "TrackingReference": tracking_reference,
        }
        return self.api_call(service_type=ServiceType.PURCHASE_BILL, data=data)

    def get_bill_purchase_status(
        self, bill_response_reference: str, bill_request_reference: str
    ):
        data = {
            "BillResponseReference": bill_response_reference,
            "BillRequestRef": bill_request_reference,
        }
        return self.api_call(service_type=ServiceType.BILL_TSQ, data=data)

    def get_purchased_bills(self):
        """Get bills purchased from the main account"""
        return self.api_call(service_type=ServiceType.ADMIN_GET_PURCHASED_BILLS)

    def get_purchased_bill_from_virtual_account(self, tracking_reference: str):
        data = {"TrackingReference": tracking_reference}
        return self.api_call(service_type=ServiceType.GET_PURCHASED_BILLS, data=data)
