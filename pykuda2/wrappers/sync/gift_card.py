from typing import Optional

from pykuda2.base import BaseAPIWrapper
from pykuda2.utils import ServiceType


class GiftCard(BaseAPIWrapper):
    def gift_cards(self):
        """Get a curated list of gift cards supported."""
        return self.api_call(service_type=ServiceType.GET_GIFT_CARD)

    def purchase_gift_card(
        self,
        amount: int,
        customer_name: str,
        customer_mobile: str,
        customer_email: str,
        biller_identifier: str,
        note: Optional[str] = None,
    ):
        """Buy gift cards from the admin account"""
        data = {
            "amount": amount,
            "requestingCustomerName": customer_name,
            "requestingCustomerMobile": customer_mobile,
            "requestingCustomerEmail": customer_email,
            "billerIdentifier": biller_identifier,
            "note": note,
        }
        return self.api_call(service_type=ServiceType.ADMIN_BUY_GIFT_CARD, data=data)

    def purchase_gift_card_from_virtual_account(
        self,
        tracking_reference: str,
        amount: int,
        customer_name: str,
        customer_mobile: str,
        customer_email: str,
        biller_identifier: str,
        note: Optional[str] = None,
    ):
        """Buy gift cards from the virtual account"""
        data = {
            "trackingReference": tracking_reference,
            "amount": amount,
            "requestingCustomerName": customer_name,
            "requestingCustomerMobile": customer_mobile,
            "requestingCustomerEmail": customer_email,
            "billerIdentifier": biller_identifier,
            "note": note,
        }
        return self.api_call(service_type=ServiceType.BUY_GIFT_CARD, data=data)

    def get_gift_card_status(
        self,
        tracking_reference: str,
        amount: int,
        customer_name: str,
        customer_mobile: str,
        customer_email: str,
        biller_identifier: str,
        note: str,
    ):
        """Status of all gift cards purchased"""
        data = {
            "trackingReference": tracking_reference,
            "amount": amount,
            "requestingCustomerName": customer_name,
            "requestingCustomerMobile": customer_mobile,
            "requestingCustomerEmail": customer_email,
            "billerIdentifier": biller_identifier,
            "note": note,
        }
        return self.api_call(service_type=ServiceType.GIFT_CARD_TSQ, data=data)
