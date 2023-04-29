from unittest import TestCase

from httpx import codes as HTTP_STATUS_CODE

from pykuda2.wrappers.sync_wrappers.gift_card import GiftCard
from tests.mocked_api_call_testcase import CredentialMixin, MockedAPICallTestCase


class MockedGiftCardTestCase(MockedAPICallTestCase):
    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()
        cls.wrapper = GiftCard(email=cls.email, api_key=cls.api_key)

    def test_can_gift_cards(self):
        response = self.wrapper.get_gift_cards()
        self.assertEqual(response.status_code, HTTP_STATUS_CODE.OK)
        self.assertTrue(response.status)

    def test_can_purchase_gift_card(self):
        # TODO: Test properly
        response = self.wrapper.purchase_gift_card(
            amount=5000,
            customer_name="John Doe",
            customer_mobile="09012345678",
            customer_email="johndoe@example.com",
            biller_identifier="KUD-GFTC-UAE-002",
        )
        self.assertEqual(response.status_code, HTTP_STATUS_CODE.OK)

    def test_can_purchase_gift_card_from_virtual_account(self):
        response = self.wrapper.purchase_gift_card_from_virtual_account(
            tracking_reference="qwerty",
            amount=5000,
            customer_name="John Doe",
            customer_email="johndoe@example.com",
            customer_mobile="09023123243",
            biller_identifier="KUD-GFTC-UAE-002",
        )
        self.assertEqual(response.status_code, HTTP_STATUS_CODE.OK)

    def test_can_get_gift_card_status(self):
        # TODO: Test properly
        response = self.wrapper.get_gift_card_status(
            tracking_reference="qwerty",
            amount=5000,
            customer_name="John Doe",
            customer_mobile="09034957384",
            customer_email="johndoe@example.com",
            biller_identifier="KUD-GFTC-UAE-002",
        )
        self.assertEqual(response.status_code, HTTP_STATUS_CODE.OK)


class GiftCardTestCase(CredentialMixin, TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()
        cls.wrapper = GiftCard(email=cls.email, api_key=cls.api_key)

    def test_can_gift_cards(self):
        response = self.wrapper.get_gift_cards()
        self.assertEqual(response.status_code, HTTP_STATUS_CODE.OK)
        self.assertTrue(response.status)

    def test_can_purchase_gift_card(self):
        # TODO: Test properly
        response = self.wrapper.purchase_gift_card(
            amount=5000,
            customer_name="John Doe",
            customer_mobile="09012345678",
            customer_email="johndoe@example.com",
            biller_identifier="KUD-GFTC-UAE-002",
        )
        self.assertEqual(response.status_code, HTTP_STATUS_CODE.OK)

    def test_can_purchase_gift_card_from_virtual_account(self):
        response = self.wrapper.purchase_gift_card_from_virtual_account(
            tracking_reference="qwerty",
            amount=5000,
            customer_name="John Doe",
            customer_email="johndoe@example.com",
            customer_mobile="09023123243",
            biller_identifier="KUD-GFTC-UAE-002",
        )
        self.assertEqual(response.status_code, HTTP_STATUS_CODE.OK)

    def test_can_get_gift_card_status(self):
        # TODO: Test properly
        response = self.wrapper.get_gift_card_status(
            tracking_reference="qwerty",
            amount=5000,
            customer_name="John Doe",
            customer_mobile="09034957384",
            customer_email="johndoe@example.com",
            biller_identifier="KUD-GFTC-UAE-002",
        )
        self.assertEqual(response.status_code, HTTP_STATUS_CODE.OK)
