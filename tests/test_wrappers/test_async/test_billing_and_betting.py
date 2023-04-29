from unittest import IsolatedAsyncioTestCase

from pykuda2 import BillType
from pykuda2.wrappers.async_wrappers.billing_and_betting import AsyncBillingAndBetting
from tests.mocked_api_call_testcase import MockedAsyncAPICallTestCase, CredentialMixin
from httpx import codes as HTTP_STATUS_CODE


class MockedAsyncBillingAndBettingTestCase(MockedAsyncAPICallTestCase):
    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()
        cls.wrapper = AsyncBillingAndBetting(email=cls.email, api_key=cls.api_key)

    async def test_can_get_bill_type_options(self):
        response = await self.wrapper.get_bill_type_options(
            bill_type=BillType.INTERNET_DATA
        )
        self.assertEqual(response.status_code, HTTP_STATUS_CODE.OK)
        self.assertEqual(
            response.message,
            "This is a mocked response. No real API call to Kuda servers was made.",
        )

    async def test_can_verify_customer_before_purchase(self):
        # TODO: Properly test this method.
        response = await self.wrapper.verify_customer_before_purchase(
            tracking_reference="",
            kuda_bill_item_identifier="",
            customer_identification="",
        )
        self.assertEqual(response.status_code, HTTP_STATUS_CODE.OK)

    async def test_can_purchase_bill(self):
        # TODO: Properly test this method.
        response = await self.wrapper.purchase_bill(
            amount=5000, bill_item_identifier="", customer_identifier=""
        )
        self.assertEqual(response.status_code, HTTP_STATUS_CODE.OK)

    async def test_can_purchase_bill_from_virtual_account(self):
        # TODO: Properly test this method.
        response = await self.wrapper.purchase_bill_from_virtual_account(
            tracking_reference="qwerty",
            amount=5000,
            bill_item_identifier="",
            phone_number="",
            customer_identifier="",
        )
        self.assertEqual(response.status_code, HTTP_STATUS_CODE.OK)

    async def test_can_get_bill_purchase_status(self):
        # TODO: Properly test this method.
        response = await self.wrapper.get_bill_purchase_status(
            bill_response_reference="qwery", bill_request_ref=None
        )
        self.assertEqual(response.status_code, HTTP_STATUS_CODE.OK)

    async def test_can_get_purchased_bills(self):
        response = await self.wrapper.get_purchased_bills()
        self.assertEqual(response.status_code, HTTP_STATUS_CODE.OK)
        self.assertTrue(response.status)

    async def test_can_get_purchased_bill_from_virtual_account(self):
        response = await self.wrapper.get_purchased_bill_from_virtual_account(
            tracking_reference="qwerty"
        )
        self.assertEqual(response.status_code, HTTP_STATUS_CODE.OK)
        self.assertTrue(response.status)


class AsyncBillingAndBettingTestCase(CredentialMixin, IsolatedAsyncioTestCase):
    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()
        cls.wrapper = AsyncBillingAndBetting(email=cls.email, api_key=cls.api_key)

    async def test_can_get_bill_type_options(self):
        response = await self.wrapper.get_bill_type_options(
            bill_type=BillType.INTERNET_DATA
        )
        self.assertEqual(response.status_code, HTTP_STATUS_CODE.OK)
        self.assertEqual(response.message, "Bill type record not found")

    async def test_can_verify_customer_before_purchase(self):
        # TODO: Properly test this method.
        response = await self.wrapper.verify_customer_before_purchase(
            tracking_reference="",
            kuda_bill_item_identifier="",
            customer_identification="",
        )
        self.assertEqual(response.status_code, HTTP_STATUS_CODE.OK)

    async def test_can_purchase_bill(self):
        # TODO: Properly test this method.
        response = await self.wrapper.purchase_bill(
            amount=5000, bill_item_identifier="", customer_identifier=""
        )
        self.assertEqual(response.status_code, HTTP_STATUS_CODE.OK)

    async def test_can_purchase_bill_from_virtual_account(self):
        # TODO: Properly test this method.
        response = await self.wrapper.purchase_bill_from_virtual_account(
            tracking_reference="qwerty",
            amount=5000,
            bill_item_identifier="",
            phone_number="",
            customer_identifier="",
        )
        self.assertEqual(response.status_code, HTTP_STATUS_CODE.OK)

    async def test_can_get_bill_purchase_status(self):
        # TODO: Properly test this method.
        response = await self.wrapper.get_bill_purchase_status(
            bill_response_reference="qwery", bill_request_ref=None
        )
        self.assertEqual(response.status_code, HTTP_STATUS_CODE.OK)

    async def test_can_get_purchased_bills(self):
        response = await self.wrapper.get_purchased_bills()
        self.assertEqual(response.status_code, HTTP_STATUS_CODE.OK)
        self.assertTrue(response.status)

    async def test_can_get_purchased_bill_from_virtual_account(self):
        response = await self.wrapper.get_purchased_bill_from_virtual_account(
            tracking_reference="qwerty"
        )
        self.assertEqual(response.status_code, HTTP_STATUS_CODE.OK)
        self.assertTrue(response.status)
