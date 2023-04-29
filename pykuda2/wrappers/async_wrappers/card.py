from typing import Optional

from pykuda2.base import BaseAsyncAPIWrapper
from pykuda2.utils import ServiceType, CardChannel, Gender, APIResponse


class AsyncCard(BaseAsyncAPIWrapper):
    async def request_card(
        self,
        tracking_reference: str,
        name_on_card: str,
        country: str,
        gender: Gender,
        additional_phone_number: str,
        delivery_city: str,
        delivery_lga: str,
        delivery_landmark: str,
        date_of_birth: str,
        delivery_state: str,
        delivery_street_no_and_name: str,
        request_reference: Optional[str] = None,
    ) -> APIResponse:
        """Request for a new card for a customer and get it delivered to their location.

        Args:
            tracking_reference: The unique identifier of the virtual account.
            name_on_card: The virtual account name.
            date_of_birth: The customer's date of birth. Format(YYYY-MM-DD).
            gender: Customer's gender e.g. Gender.MALE, Gender.FEMALE.
            delivery_state: The state of residence for card delivery.
            delivery_street_no_and_name: The street no and name for card delivery.
            delivery_city: Name of city for card delivery.
            delivery_lga: Local government area for card delivery
            delivery_landmark: Landmark for card delivery.
            country: Country of residence for card delivery.
            additional_phone_number: additional phone number.
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
        return await self._api_call(
            service_type=ServiceType.REQUEST_CARD,
            data=data,
            # endpoint_path="/RequestCard",
            request_reference=request_reference,
        )

    async def get_cards(
        self,
        tracking_reference: str,
        simulate_request: bool = False,
        request_reference: Optional[str] = None,
    ) -> APIResponse:
        """Retrieves a list of cards requested.

        Args:
            tracking_reference: The unique identifier of the account.
            simulate_request: Flag to simulate request.
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
            "SimulateRequest": simulate_request,
        }
        return await self._api_call(
            service_type=ServiceType.GET_CUSTOMER_CARDS,
            data=data,
            # endpoint_path="/GetCustomerCards",
            request_reference=request_reference,
        )

    async def activate_card(
        self,
        pan: int,
        cvv: int,
        id: int,
        tracking_reference: str,
        simulate_request: bool = False,
        request_reference: Optional[str] = None,
    ) -> APIResponse:
        """Allows customers activate their cards once they receive it.

        Args:
            pan: Card primary account number issued after processing.
            cvv: Card CVV.
            tracking_reference: The unique identifier of the account.
            id: Card unique identifier.
            simulate_request: Flag to simulate request.
            request_reference: a unique identifier for this api call.
                it is automatically generated if not provided.

        Returns:
            An `APIResponse` which is basically just a dataclass containing the data returned by the server as result
                of calling this function.

        Raises:
            ConnectionException: when the request times out or in the absence of an internet connection.
        """
        data = {
            "Pan": pan,
            "CVV": cvv,
            "Id": id,
            "TrackingReference": tracking_reference,
            "SimulateRequest": simulate_request,
        }
        return await self._api_call(
            service_type=ServiceType.ACTIVATE_CARD,
            data=data,
            # endpoint_path="/ActivateCard",
            request_reference=request_reference,
        )

    async def deactivate_card(
        self,
        id: int,
        tracking_reference: str,
        simulate_request: bool = False,
        request_reference: Optional[str] = None,
    ) -> APIResponse:
        """Allows customers deactivate their cards.

        Args:
            tracking_reference: The unique identifier of the account.
            id: Card unique identifier.
            simulate_request: Flag to simulate request.
            request_reference: a unique identifier for this api call.
                it is automatically generated if not provided.

        Returns:
            An `APIResponse` which is basically just a dataclass containing the data returned by the server as result
                of calling this function.

        Raises:
            ConnectionException: when the request times out or in the absence of an internet connection.
        """
        data = {
            "Id": id,
            "TrackingReference": tracking_reference,
            "SimulateRequest": simulate_request,
        }
        return await self._api_call(
            service_type=ServiceType.DEACTIVATE_CARD,
            data=data,
            # endpoint_path="/DeactivateCard",
            request_reference=request_reference,
        )

    async def set_card_limit(
        self,
        id: int,
        tracking_reference: str,
        channel: CardChannel,
        limit: int,
        simulate_request: bool = False,
        request_reference: Optional[str] = None,
    ) -> APIResponse:
        """Set spend limit on a card.

        Card limits are a good way to manage individual spend on their accounts.
        There are use cases for this, especially in the edtech space where an individual
        will like to manage spending limits or even in the contracting space where clients
        want to manage spend limits on purchases.
            - A good way to start this is to manage where and how these limits can be set
                and across the channels the card can be accessed.

        Args:
            id: Card unique identifier.
            tracking_reference: The virtual account number.
            channel: Card channels e.g. CardChannel.ATM, CardChannel.POS.
            limit: Transaction amount limit in kobo.
            simulate_request: Flag to simulate request.
            request_reference: a unique identifier for this api call.
                it is automatically generated if not provided.

        Returns:
            An `APIResponse` which is basically just a dataclass containing the data returned by the server as result
                of calling this function.

        Raises:
            ConnectionException: when the request times out or in the absence of an internet connection.
        """
        data = {
            "Id": id,
            "TrackingReference": tracking_reference,
            "Channel": channel,
            "Limit": limit,
            "SimulateRequest": simulate_request,
        }
        return await self._api_call(
            service_type=ServiceType.MANAGE_CARD_TRANSACTION_LIMIT,
            data=data,
            # endpoint_path="/ManageCardTransactionLimit",
            request_reference=request_reference,
        )

    async def manage_card_channel(
        self,
        id: int,
        tracking_reference: str,
        channel: CardChannel,
        limit: int,
        simulate_request: bool = False,
        request_reference: Optional[str] = None,
    ) -> APIResponse:
        """Allows customers manage where their cards can be used.

        Args:
            id: Card unique identifier.
            tracking_reference: The virtual account number.
            channel: Card channels e.g. CardChannel.ATM, CardChannel.POS.
            limit: Transaction amount limit in kobo.
            simulate_request: Flag to simulate request.
            request_reference: a unique identifier for this api call.
                it is automatically generated if not provided.

        Returns:
            An `APIResponse` which is basically just a dataclass containing the data returned by the server as result
                of calling this function.

        Raises:
            ConnectionException: when the request times out or in the absence of an internet connection.
        """
        data = {
            "Id": id,
            "TrackingReference": tracking_reference,
            "Channel": channel,
            "Limit": limit,
            "SimulateRequest": simulate_request,
        }
        return await self._api_call(
            service_type=ServiceType.MANAGE_CARD_CHANNEL,
            data=data,
            # endpoint_path="/ManageCardChannel",
            request_reference=request_reference,
        )

    async def change_card_pin(
        self,
        id: int,
        tracking_reference: str,
        new_pin: int,
        request_reference: Optional[str] = None,
    ) -> APIResponse:
        """Allows customers change their 4 digits PIN to any combination they desire.

        Args:
            id: Card unique identifier.
            tracking_reference: The virtual account number.
            new_pin: Customer's new PIN.
            request_reference: a unique identifier for this api call.
                it is automatically generated if not provided.

        Returns:
            An `APIResponse` which is basically just a dataclass containing the data returned by the server as result
                of calling this function.

        Raises:
            ConnectionException: when the request times out or in the absence of an internet connection."""
        data = {"Id": id, "TrackingReference": tracking_reference, "NewPIN": new_pin}
        return await self._api_call(
            service_type=ServiceType.CHANGE_CARD_PIN,
            data=data,
            # endpoint_path="/ChangeCardPIN",
            request_reference=request_reference,
        )

    async def block_card(
        self, tracking_reference: str, id: int, request_reference: Optional[str] = None
    ) -> APIResponse:
        """Block a customer's card.

        It allows them to longer be able to make card transactions with it.
        In an emergency, a user may require to block a card in the event that the
        card is stolen or lost. Use this method to quickly block the card.

        Args:
            id: Card unique identifier.
            tracking_reference: The virtual account number.
            request_reference: a unique identifier for this api call.
                it is automatically generated if not provided.

        Returns:
            An `APIResponse` which is basically just a dataclass containing the data returned by the server as result
                of calling this function.

        Raises:
            ConnectionException: when the request times out or in the absence of an internet connection.
        """
        data = {
            "Id": id,
            "TrackingReference": tracking_reference,
        }
        return await self._api_call(
            service_type=ServiceType.BLOCK_CARD,
            data=data,
            # endpoint_path="/BlockCard",
            request_reference=request_reference,
        )

    async def unblock_card(
        self, tracking_reference: str, id: int, request_reference: Optional[str] = None
    ) -> APIResponse:
        """Unblocks a customers card.

        Args:
            id: Card unique identifier.
            tracking_reference: The virtual account number.
            request_reference: a unique identifier for this api call.
                it is automatically generated if not provided.

        Returns:
            An `APIResponse` which is basically just a dataclass containing the data returned by the server as result
                of calling this function.

        Raises:
            ConnectionException: when the request times out or in the absence of an internet connection.
        """
        data = {
            "Id": id,
            "TrackingReference": tracking_reference,
        }
        return await self._api_call(
            service_type=ServiceType.UNBLOCK_CARD,
            data=data,
            # endpoint_path="/UnblockCard",
            request_reference=request_reference,
        )
