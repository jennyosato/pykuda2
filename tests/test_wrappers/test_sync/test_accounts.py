from unittest import TestCase
from uuid import uuid4

from pykuda2.utils import generate_number
from pykuda2.wrappers.sync_wrappers.accounts import Account
from tests.mocked_api_call_testcase import MockedAPICallTestCase, CredentialMixin
from httpx import codes as HTTP_STATUS_CODE


class MockedAccountTesCase(MockedAPICallTestCase):
    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()
        cls.wrapper = Account(email=cls.email, api_key=cls.api_key)

    def test_can_create_virtual_account(self):
        response = self.wrapper.create_virtual_account(
            email=f"johndoe{generate_number(10)}@example.com",
            phone_number=f"070{generate_number(8)}",
            last_name="Doe",
            first_name="John",
            middle_name="",
            business_name="",
            tracking_reference=str(generate_number(10)),
        )
        self.assertEqual(response.status_code, HTTP_STATUS_CODE.OK)
        self.assertTrue(response.status)

    def test_can_update_virtual_account(self):
        tracking_reference = str(generate_number(10))
        self.wrapper.create_virtual_account(
            email=f"johndoe{generate_number(10)}@example.com",
            phone_number=f"070{generate_number(8)}",
            last_name="Doe",
            first_name="John",
            middle_name="",
            business_name="",
            tracking_reference=tracking_reference,
        )
        response = self.wrapper.update_virtual_account(
            tracking_reference=tracking_reference,
            first_name="Gbenga",
            last_name="Adeyi",
        )
        self.assertEqual(response.status_code, HTTP_STATUS_CODE.OK)
        self.assertTrue(response.status)

    def test_can_get_virtual_accounts(self):
        response = self.wrapper.get_virtual_accounts(page_size=50, page_number=1)
        self.assertEqual(response.status_code, HTTP_STATUS_CODE.OK)
        self.assertTrue(response.status)

    def test_can_get_virtual_account(self):
        response = self.wrapper.get_virtual_account(tracking_reference="qwerty")
        self.assertEqual(response.status_code, HTTP_STATUS_CODE.OK)
        self.assertTrue(response.status)

    def test_can_disable_virtual_account(self):
        response = self.wrapper.disable_virtual_account(tracking_reference="9466500772")
        self.assertEqual(response.status_code, HTTP_STATUS_CODE.OK)
        self.assertTrue(response.status)

    def test_can_enable_virtual_account(self):
        response = self.wrapper.enable_virtual_account(tracking_reference="264977600")
        self.assertEqual(response.status_code, HTTP_STATUS_CODE.OK)
        self.assertTrue(response.status)

    def test_can_get_admin_account_balance(self):
        response = self.wrapper.get_admin_account_balance()
        self.assertEqual(response.status_code, HTTP_STATUS_CODE.OK)
        self.assertTrue(response.status)

    def test_can_get_virtual_account_balance(self):
        response = self.wrapper.get_virtual_account_balance(
            tracking_reference="264977600"
        )
        self.assertEqual(response.status_code, HTTP_STATUS_CODE.OK)
        self.assertTrue(response.status)


class AccountTesCase(CredentialMixin, TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()
        cls.wrapper = Account(email=cls.email, api_key=cls.api_key)

    def test_can_create_virtual_account(self):
        response = self.wrapper.create_virtual_account(
            email=f"johndoe{generate_number(10)}@example.com",
            phone_number=f"070{generate_number(8)}",
            last_name="Doe",
            first_name="John",
            middle_name="",
            business_name="",
            tracking_reference=str(generate_number(10)),
        )
        self.assertEqual(response.status_code, HTTP_STATUS_CODE.OK)
        self.assertTrue(response.status)

    def test_can_update_virtual_account(self):
        tracking_reference = str(generate_number(10))
        self.wrapper.create_virtual_account(
            email=f"johndoe{generate_number(10)}@example.com",
            phone_number=f"070{generate_number(8)}",
            last_name="Doe",
            first_name="John",
            middle_name="",
            business_name="",
            tracking_reference=tracking_reference,
        )
        response = self.wrapper.update_virtual_account(
            tracking_reference=tracking_reference,
            first_name="Gbenga",
            last_name="Adeyi",
        )
        self.assertEqual(response.status_code, HTTP_STATUS_CODE.OK)
        self.assertTrue(response.status)

    def test_can_get_virtual_accounts(self):
        response = self.wrapper.get_virtual_accounts(page_size=50, page_number=1)
        self.assertEqual(response.status_code, HTTP_STATUS_CODE.OK)
        self.assertTrue(response.status)

    def test_can_get_virtual_account(self):
        response = self.wrapper.get_virtual_account(tracking_reference="qwerty")
        self.assertEqual(response.status_code, HTTP_STATUS_CODE.OK)
        self.assertTrue(response.status)

    def test_can_disable_virtual_account(self):
        response = self.wrapper.disable_virtual_account(tracking_reference="9466500772")
        self.assertEqual(response.status_code, HTTP_STATUS_CODE.OK)
        self.assertTrue(response.status)

    def test_can_enable_virtual_account(self):
        response = self.wrapper.enable_virtual_account(tracking_reference="264977600")
        self.assertEqual(response.status_code, HTTP_STATUS_CODE.OK)
        self.assertTrue(response.status)

    def test_can_get_admin_account_balance(self):
        response = self.wrapper.get_admin_account_balance()
        self.assertEqual(response.status_code, HTTP_STATUS_CODE.OK)
        self.assertTrue(response.status)

    def test_can_get_virtual_account_balance(self):
        response = self.wrapper.get_virtual_account_balance(
            tracking_reference="264977600"
        )
        self.assertEqual(response.status_code, HTTP_STATUS_CODE.OK)
        self.assertTrue(response.status)
