from pykuda2.base import APIWrapper, ServiceType


class Billing_and_Betting(APIWrapper):
    def get_bill_type(self, bill_type_name:str):
        data = {
            "BillTypeName": bill_type_name
        }
        return self.api_call(service_type=ServiceType.GET_BILLERS_BY_TYPE, data=data)
    def verify_customer_before_purchase(self,track_ref:str,kuda_bill_item_identifier:str, customer_identification:str ):
        data = {
              "TrackingRef": track_ref,
             "KudaBillItemIdentifier":kuda_bill_item_identifier,
             "CustomerIdentification":customer_identification
        }
        return self.api_call(service_type=ServiceType.VERIFY_BILL_CUSTOMER, data=data)
    def admin_purchase_bill(self, amount:int, bill_item_identifier:str, phone_number:str, customer_identifier:str):
        data = {
            "Amount":amount,
	        "BillItemIdentifier":bill_item_identifier,
	        "PhoneNumber": phone_number,
	        "CustomerIdentifier": customer_identifier
            }
        return self.api_call(service_type=ServiceType.ADMIN_PURCHASE_BILL, data=data)
    def virtual_purchase_bill(self,tracking_reference:str, amount:int, bill_item_identifier:str, phone_number:str, customer_identifier:str):
        data = {
            "Amount":amount,
	        "BillItemIdentifier":bill_item_identifier,
	        "PhoneNumber": phone_number,
	        "CustomerIdentifier": customer_identifier,
            "TrackingReference": tracking_reference
        }
        return self.api_call(service_type=ServiceType.PURCHASE_BILL, data=data)
    def get_bill_purchase_status(self, bill_response_reference: str, bill_request_ref:str):
        data = {
            "BillResponseReference":bill_response_reference,
	        "BillRequestRef":bill_request_ref
        }
        return self.api_call(service_type=ServiceType.BILL_TSQ, data=data)
    def get_admin_purchased_bill(self):
        return self.api_call(service_type=ServiceType.ADMIN_GET_PURCHASED_BILLS)
    
    def get_virtual_purchased_bill(self,tracking_reference: str):
        data = {"TrackingReferencs": tracking_reference}
        return self.api_call(service_type=ServiceType.GET_PURCHASED_BILLS, data=data)