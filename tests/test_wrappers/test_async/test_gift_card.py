from unittest import IsolatedAsyncioTestCase

from httpx import codes as HTTP_STATUS_CODE

from pykuda2.wrappers.async_wrappers.gift_card import AsyncGiftCard
from tests.mocked_api_call_testcase import CredentialMixin, MockedAsyncAPICallTestCase


class MockedAsyncGiftCardTestCase(MockedAsyncAPICallTestCase):
    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()
        cls.wrapper = AsyncGiftCard(email=cls.email, api_key=cls.api_key)

    async def test_can_gift_cards(self):
        response = await self.wrapper.gift_cards()
        self.assertEqual(response.status_code, HTTP_STATUS_CODE.OK)
        self.assertTrue(response.status)

    async def test_can_purchase_gift_card(self):
        # TODO: Test properly
        response = await self.wrapper.purchase_gift_card(
            amount=5000,
            customer_name="John Doe",
            customer_mobile="09012345678",
            customer_email="johndoe@example.com",
            biller_identifier="KUD-GFTC-UAE-002",
        )
        self.assertEqual(response.status_code, HTTP_STATUS_CODE.OK)

    async def test_can_purchase_gift_card_from_virtual_account(self):
        response = await self.wrapper.purchase_gift_card_from_virtual_account(
            tracking_reference="qwerty",
            amount=5000,
            customer_name="John Doe",
            customer_email="johndoe@example.com",
            customer_mobile="09023123243",
            biller_identifier="KUD-GFTC-UAE-002",
        )
        self.assertEqual(response.status_code, HTTP_STATUS_CODE.OK)

    async def test_can_get_gift_card_status(self):
        # TODO: Test properly
        response = await self.wrapper.get_gift_card_status(
            tracking_reference="qwerty",
            amount=5000,
            customer_name="John Doe",
            customer_mobile="09034957384",
            customer_email="johndoe@example.com",
            biller_identifier="KUD-GFTC-UAE-002",
        )
        self.assertEqual(response.status_code, HTTP_STATUS_CODE.OK)


class AsyncGiftCardTestCase(CredentialMixin, IsolatedAsyncioTestCase):
    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()
        cls.wrapper = AsyncGiftCard(email=cls.email, api_key=cls.api_key)

    async def test_can_gift_cards(self):
        response = await self.wrapper.gift_cards()
        self.assertEqual(response.status_code, HTTP_STATUS_CODE.OK)
        self.assertTrue(response.status)

    async def test_can_purchase_gift_card(self):
        # TODO: Test properly
        response = await self.wrapper.purchase_gift_card(
            amount=5000,
            customer_name="John Doe",
            customer_mobile="09012345678",
            customer_email="johndoe@example.com",
            biller_identifier="KUD-GFTC-UAE-002",
        )
        self.assertEqual(response.status_code, HTTP_STATUS_CODE.OK)

    async def test_can_purchase_gift_card_from_virtual_account(self):
        response = await self.wrapper.purchase_gift_card_from_virtual_account(
            tracking_reference="qwerty",
            amount=5000,
            customer_name="John Doe",
            customer_email="johndoe@example.com",
            customer_mobile="09023123243",
            biller_identifier="KUD-GFTC-UAE-002",
        )
        self.assertEqual(response.status_code, HTTP_STATUS_CODE.OK)

    async def test_can_get_gift_card_status(self):
        # TODO: Test properly
        response = await self.wrapper.get_gift_card_status(
            tracking_reference="qwerty",
            amount=5000,
            customer_name="John Doe",
            customer_mobile="09034957384",
            customer_email="johndoe@example.com",
            biller_identifier="KUD-GFTC-UAE-002",
        )
        self.assertEqual(response.status_code, HTTP_STATUS_CODE.OK)
