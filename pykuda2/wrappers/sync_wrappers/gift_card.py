from typing import Optional

from pykuda2.base import BaseAPIWrapper
from pykuda2.utils import ServiceType, APIResponse


class GiftCard(BaseAPIWrapper):
    def get_gift_cards(self, request_reference: Optional[str] = None) -> APIResponse:
        """Retrieves a curated list of gift cards supported by Kuda.

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
            service_type=ServiceType.GET_GIFT_CARD, request_reference=request_reference
        )

    def purchase_gift_card(
        self,
        amount: int,
        customer_name: str,
        customer_mobile: str,
        customer_email: str,
        biller_identifier: str,
        note: Optional[str] = None,
        request_reference: Optional[str] = None,
    ) -> APIResponse:
        """Buy gift cards from the admin account

        Args:
            amount: The gift card amount to be purchased. It could be in USD/ GBP/ EUR/ NGN/ AED , e.t.c.
            customer_name: Name of the customer receiving the gift card.
            customer_mobile: Mobile number of customer.
            customer_email: The email address of customer.
            biller_identifier: The Biller ID or identifier. You can find it in the `APIResponse` of
                `self.gift_cards`.
            note: An optional gift card note.
            request_reference: a unique identifier for this api call.
                it is automatically generated if not provided.

        Returns:
            An `APIResponse` which is basically just a dataclass containing the data returned by the server as result
                of calling this function.

        Raises:
            ConnectionException: when the request times out or in the absence of an internet connection.
        """
        data = {
            "amount": amount,
            "requestingCustomerName": customer_name,
            "requestingCustomerMobile": customer_mobile,
            "requestingCustomerEmail": customer_email,
            "billerIdentifier": biller_identifier,
            "note": note,
        }
        return self._api_call(
            service_type=ServiceType.ADMIN_BUY_GIFT_CARD,
            data=data,
            request_reference=request_reference,
        )

    def purchase_gift_card_from_virtual_account(
        self,
        tracking_reference: str,
        amount: int,
        customer_name: str,
        customer_mobile: str,
        customer_email: str,
        biller_identifier: str,
        note: Optional[str] = None,
        request_reference: Optional[str] = None,
    ) -> APIResponse:
        """Buy gift cards from the virtual account.

        Args:
            tracking_reference: The unique identifier of the virtual account.
            amount: The gift card amount to be purchased. It could be in USD/ GBP/ EUR/ NGN/ AED , e.t.c.
            customer_name: Name of the customer receiving the gift card.
            customer_mobile: Mobile number of customer.
            customer_email: The email address of customer.
            biller_identifier: The Biller ID or identifier. You can find it in the `APIResponse` of
                `self.gift_cards`.
            note: An optional gift card note.
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
            "requestingCustomerName": customer_name,
            "requestingCustomerMobile": customer_mobile,
            "requestingCustomerEmail": customer_email,
            "billerIdentifier": biller_identifier,
            "note": note,
        }
        return self._api_call(
            service_type=ServiceType.BUY_GIFT_CARD,
            data=data,
            request_reference=request_reference,
        )

    def get_gift_card_status(
        self,
        tracking_reference: str,
        amount: int,
        customer_name: str,
        customer_mobile: str,
        customer_email: str,
        biller_identifier: str,
        note: Optional[str] = None,
        request_reference: Optional[str] = None,
    ) -> APIResponse:
        """Retrieves the status of all gift cards purchased.

        Args:
            tracking_reference: The unique identifier of the virtual account.
            amount: The gift card amount to be purchased. It could be in USD/ GBP/ EUR/ NGN/ AED , e.t.c.
            customer_name: Name of the customer receiving the gift card.
            customer_mobile: Mobile number of customer.
            customer_email: The email address of customer.
            biller_identifier: The Biller ID or identifier. You can find it in the `APIResponse` of
                `self.gift_cards`.
            note: An optional gift card note.
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
            "requestingCustomerName": customer_name,
            "requestingCustomerMobile": customer_mobile,
            "requestingCustomerEmail": customer_email,
            "billerIdentifier": biller_identifier,
            "note": note,
        }
        return self._api_call(
            service_type=ServiceType.GIFT_CARD_TSQ,
            data=data,
            request_reference=request_reference,
        )
