from pykuda2.base import APIWrapper, ServiceType


class Cards(APIWrapper):
    def request_card(self, delivery_city:str, delivery_lga:str, delivery_landmark:str,country:str, additional_phone_number:str, tracking_reference:str, name_on_card: str, date_of_birth:str, gender:int, delivery_state:str,delivery_street_no_and_name:str,):
        data = {
            "TrackingReference": tracking_reference,
            "NameOnCard": name_on_card,
            "DateofBirth": date_of_birth,
            "Gender": gender,
            "DeliveryState": delivery_state,
            "DeliveryStreetNoAndName": delivery_street_no_and_name,
            "DeliveryCity": delivery_city,
            "DeliveryLGA": delivery_lga,
            "DeliveryLandmark": delivery_landmark,
            "Country": country,
            "CdditionalPhoneNumber": additional_phone_number
        }
        return self.api_call(service_type=ServiceType.REQUEST_CARD, data=data)
    def get_cards(self, simulate_request, tracking_reference:str):
        """Gets a list of card requested"""
        data = {
            "TrackingReference": tracking_reference,
		    "SimulateRequest": simulate_request
        }
        return self.api_call(service_type=ServiceType.GET_CUSTOMER_CARDS, data=data)
    def activate_card(self, pan:int, cvv:int,id:int, tracking_reference:str, simulate_request):
        data = {
            "Pan": pan,
		    "CVV": cvv,
		    "Id": id,
		    "TrackingReference": tracking_reference,
		    "SimulateRequest": simulate_request
        }
        return self.api_call(service_type=ServiceType.ACTIVATE_CARD, data=data)
    def deactivate_card(self, id:int, tracking_reference:str, simulate_request):
        data = {
		    "Id": id,
		    "TrackingReference": tracking_reference,
		    "SimulateRequest": simulate_request
        }
        return self.api_call(service_type=ServiceType.DEACTIVATE_CARD, data=data)
    def set_card_limit(self, channel:int, limit:int, id:int, tracking_reference:str, simulate_request:str):
        data = {
            "Id": id,
		    "TrackingReference": tracking_reference,
            "Channel": channel,
		    "Limit": limit,
		    "SimulateRequest": simulate_request
        }
        return self.api_call(service_type=ServiceType.MANAGE_CARD_TRANSACTION_LIMIT, data=data)
    def manage_card_channel(self, channel:int, limit:int, id:int, tracking_reference:str, simulate_request:str):
        data = {
            "Id": id,
		    "TrackingReference": tracking_reference,
            "Channel": channel,
		    "Limit": limit,
		    "SimulateRequest": simulate_request
        }
        return self.api_call(service_type=ServiceType.MANAGE_CARD_CHANNEL, data=data)
    def change_card_pin(self, tracking_reference:str, new_pin:int, id:int):
        data = {
            "Id": id,
		    "TrackingReference": tracking_reference,
		    "NewPIN": new_pin
        }
        return self.api_call(service_type=ServiceType.CHANGE_CARD_PIN, data=data)
    def block_card(self, tracking_reference:str, id:int):
        data = {
            "Id": id,
		    "TrackingReference": tracking_reference,
		    
        }
        return self.api_call(service_type=ServiceType.BLOCK_CARD, data=data)
    def unblock_card(self, tracking_reference:str, id:int):
        data = {
            "Id": id,
		    "TrackingReference": tracking_reference,  
        }
        return self.api_call(service_type=ServiceType.UNBLOCK_CARD, data=data)