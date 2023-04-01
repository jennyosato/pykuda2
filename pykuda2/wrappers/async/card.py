from pykuda2.base import BaseAsyncAPIWrapper
from pykuda2.utils import ServiceType, CardChannel


class AsyncCard(BaseAsyncAPIWrapper):
    async def request_card(
        self,
        delivery_city: str,
        delivery_lga: str,
        delivery_landmark: str,
        country: str,
        additional_phone_number: str,
        tracking_reference: str,
        name_on_card: str,
        date_of_birth: str,
        gender: int,
        delivery_state: str,
        delivery_street_no_and_name: str,
    ):
        data = {
            "TrackingReference": tracking_reference,
            "NameOnCard": name_on_card,
            "dateofBirth": date_of_birth,
            "Gender": gender,
            "DeliveryState": delivery_state,
            "DeliveryStreetNoAndName": delivery_street_no_and_name,
            "DeliveryCity": delivery_city,
            "DeliveryLGA": delivery_lga,
            "DeliveryLandmark": delivery_landmark,
            "Country": country,
            "additionalPhoneNumber": additional_phone_number,
        }
        return await self.api_call(
            service_type=ServiceType.REQUEST_CARD,
            data=data,
            endpoint_path="/RequestCard",
        )

    async def get_cards(self, simulate_request, tracking_reference: str):
        """Gets a list of card requested"""
        data = {
            "TrackingReference": tracking_reference,
            "SimulateRequest": simulate_request,
        }
        return await self.api_call(
            service_type=ServiceType.GET_CUSTOMER_CARDS,
            data=data,
            endpoint_path="/GetCustomerCards",
        )

    async def activate_card(
        self,
        pan: int,
        cvv: int,
        id: int,
        tracking_reference: str,
        simulate_request: bool,
    ):
        data = {
            "Pan": pan,
            "CVV": cvv,
            "Id": id,
            "TrackingReference": tracking_reference,
            "SimulateRequest": simulate_request,
        }
        return await self.api_call(
            service_type=ServiceType.ACTIVATE_CARD,
            data=data,
            endpoint_path="/ActivateCard",
        )

    async def deactivate_card(self, id: int, tracking_reference: str, simulate_request):
        data = {
            "Id": id,
            "TrackingReference": tracking_reference,
            "SimulateRequest": simulate_request,
        }
        return await self.api_call(
            service_type=ServiceType.DEACTIVATE_CARD,
            data=data,
            endpoint_path="/DeactivateCard",
        )

    async def set_card_limit(
        self,
        channel: int,
        limit: int,
        id: int,
        tracking_reference: str,
        simulate_request: bool,
    ):
        data = {
            "Id": id,
            "TrackingReference": tracking_reference,
            "Channel": channel,
            "Limit": limit,
            "SimulateRequest": simulate_request,
        }
        return await self.api_call(
            service_type=ServiceType.MANAGE_CARD_TRANSACTION_LIMIT,
            data=data,
            endpoint_path="/ManageCardTransactionLimit",
        )

    async def manage_card_channel(
        self,
        channel: CardChannel,
        limit: int,
        id: int,
        tracking_reference: str,
        simulate_request: bool,
    ):
        data = {
            "Id": id,
            "TrackingReference": tracking_reference,
            "Channel": channel,
            "Limit": limit,
            "SimulateRequest": simulate_request,
        }
        return await self.api_call(
            service_type=ServiceType.MANAGE_CARD_CHANNEL,
            data=data,
            endpoint_path="/ManageCardChannel",
        )

    async def change_card_pin(self, tracking_reference: str, new_pin: int, id: int):
        data = {"Id": id, "TrackingReference": tracking_reference, "NewPIN": new_pin}
        return await self.api_call(
            service_type=ServiceType.CHANGE_CARD_PIN,
            data=data,
            endpoint_path="/ChangeCardPIN",
        )

    async def block_card(self, tracking_reference: str, id: int):
        data = {
            "Id": id,
            "TrackingReference": tracking_reference,
        }
        return await self.api_call(
            service_type=ServiceType.BLOCK_CARD, data=data, endpoint_path="/BlockCard"
        )

    async def unblock_card(self, tracking_reference: str, id: int):
        data = {
            "Id": id,
            "TrackingReference": tracking_reference,
        }
        return await self.api_call(
            service_type=ServiceType.UNBLOCK_CARD,
            data=data,
            endpoint_path="/UnblockCard",
        )
