from pykuda2.base import APIWrapper, ServiceType


class Gift_Cards(APIWrapper):
    def gift_cards(self):
        """ Gets a curated list of gift cards supported.""" 
        return self.api_call(service_type=ServiceType.GET_GIFT_CARD)
    
    def buy_gift_card(self, amount:int, requesting_customer_name:str, requesting_customer_mobile:str, requesting_customer_email:str, biller_identifier:str, note:str):
        """Buy gift cards from the admin account"""
        data = {
            "amount":amount, 
	        "requestingCustomerName": requesting_customer_name,
	        "requestingCustomerMobile": requesting_customer_mobile,
	        "requestingCustomerEmail": requesting_customer_email,
	        "billerIdentifier": biller_identifier, 
	        "note": note

        }
        return self.api_call(service_type=ServiceType.ADMIN_BUY_GIFT_CARD, data=data)
    def virtual_buy_gift_card(self, tracking_reference:str, amount:int, requesting_customer_name:str, requesting_customer_mobile:str, requesting_customer_email:str, biller_identifier:str, note:str):
        """Buy gift cards from the virtual account"""
        data = {
            "trackingReference": tracking_reference,
            "amount":amount, 
	        "requestingCustomerName": requesting_customer_name,
	        "requestingCustomerMobile": requesting_customer_mobile,
	        "requestingCustomerEmail": requesting_customer_email,
	        "billerIdentifier": biller_identifier,
	        "note": note

        }
        return self.api_call(service_type=ServiceType.BUY_GIFT_CARD, data=data)
    def gift_card_status(self, tracking_reference:str, amount:int, requesting_customer_name:str, requesting_customer_mobile:str, requesting_customer_email:str, biller_identifier:str, note:str):
        """Status of all gift cards purchased"""
        data = {
            "trackingReference": tracking_reference,
            "amount":amount, 
	        "requestingCustomerName": requesting_customer_name,
	        "requestingCustomerMobile": requesting_customer_mobile,
	        "requestingCustomerEmail": requesting_customer_email,
	        "billerIdentifier": biller_identifier,
	        "note": note

        }
        return self.api_call(service_type=ServiceType.GIFT_CARD_TSQ, data=data)


    