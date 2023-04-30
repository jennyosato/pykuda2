from unittest import TestCase

from pykuda2 import BillType
from pykuda2.wrappers.sync_wrappers.billing_and_betting import BillingAndBetting
from tests.mocked_api_call_testcase import MockedAPICallTestCase, CredentialMixin
from httpx import codes as HTTP_STATUS_CODE


class MockedBillingAndBettingTestCase(MockedAPICallTestCase):
    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()
        cls.wrapper = BillingAndBetting(email=cls.email, api_key=cls.api_key)

    def test_can_get_bill_type_options(self):
        response = self.wrapper.get_bill_type_options(bill_type=BillType.INTERNET_DATA)
        self.assertEqual(response.status_code, HTTP_STATUS_CODE.OK)
        self.assertTrue(response.status)

    def test_can_verify_customer_before_purchase(self):
        response = self.wrapper.verify_customer_before_purchase(
            tracking_reference="",
            kuda_bill_item_identifier="",
            customer_identification="",
        )
        self.assertEqual(response.status_code, HTTP_STATUS_CODE.OK)
        self.assertTrue(response.status)

    def test_can_purchase_bill(self):
        response = self.wrapper.purchase_bill(
            amount=5000, bill_item_identifier="", customer_identifier=""
        )
        self.assertEqual(response.status_code, HTTP_STATUS_CODE.OK)
        self.assertTrue(response.status)

    def test_can_purchase_bill_from_virtual_account(self):
        response = self.wrapper.purchase_bill_from_virtual_account(
            tracking_reference="qwerty",
            amount=5000,
            bill_item_identifier="",
            phone_number="",
            customer_identifier="",
        )
        self.assertEqual(response.status_code, HTTP_STATUS_CODE.OK)
        self.assertTrue(response.status)

    def test_can_get_bill_purchase_status(self):
        response = self.wrapper.get_bill_purchase_status(
            bill_response_reference="qwery", bill_request_ref=None
        )
        self.assertEqual(response.status_code, HTTP_STATUS_CODE.OK)
        self.assertTrue(response.status)

    def test_can_get_purchased_bills(self):
        response = self.wrapper.get_purchased_bills()
        self.assertEqual(response.status_code, HTTP_STATUS_CODE.OK)
        self.assertTrue(response.status)

    def test_can_get_purchased_bill_from_virtual_account(self):
        response = self.wrapper.get_purchased_bill_from_virtual_account(
            tracking_reference="qwerty"
        )
        self.assertEqual(response.status_code, HTTP_STATUS_CODE.OK)
        self.assertTrue(response.status)


class BillingAndBettingTestCase(CredentialMixin, TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()
        cls.wrapper = BillingAndBetting(email=cls.email, api_key=cls.api_key)

    def test_can_get_bill_type_options(self):
        response = self.wrapper.get_bill_type_options(bill_type=BillType.INTERNET_DATA)
        self.assertEqual(response.status_code, HTTP_STATUS_CODE.OK)
        self.assertEqual(
            response.message,
            "Bill type record not found",
        )

    def test_can_verify_customer_before_purchase(self):
        # TODO: Properly test this method.
        response = self.wrapper.verify_customer_before_purchase(
            tracking_reference="",
            kuda_bill_item_identifier="",
            customer_identification="",
        )
        self.assertEqual(response.status_code, HTTP_STATUS_CODE.OK)

    def test_can_purchase_bill(self):
        # TODO: Properly test this method.
        response = self.wrapper.purchase_bill(
            amount=5000, bill_item_identifier="", customer_identifier=""
        )
        self.assertEqual(response.status_code, HTTP_STATUS_CODE.OK)

    def test_can_purchase_bill_from_virtual_account(self):
        # TODO: Properly test this method.
        response = self.wrapper.purchase_bill_from_virtual_account(
            tracking_reference="qwerty",
            amount=5000,
            bill_item_identifier="",
            phone_number="",
            customer_identifier="",
        )
        self.assertEqual(response.status_code, HTTP_STATUS_CODE.OK)

    def test_can_get_bill_purchase_status(self):
        # TODO: Properly test this method.
        response = self.wrapper.get_bill_purchase_status(
            bill_response_reference="qwery", bill_request_ref=None
        )
        self.assertEqual(response.status_code, HTTP_STATUS_CODE.OK)

    def test_can_get_purchased_bills(self):
        response = self.wrapper.get_purchased_bills()
        self.assertEqual(response.status_code, HTTP_STATUS_CODE.OK)
        self.assertTrue(response.status)

    def test_can_get_purchased_bill_from_virtual_account(self):
        response = self.wrapper.get_purchased_bill_from_virtual_account(
            tracking_reference="qwerty"
        )
        self.assertEqual(response.status_code, HTTP_STATUS_CODE.OK)
        self.assertTrue(response.status)
