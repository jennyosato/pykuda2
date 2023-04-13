from unittest import TestCase

from pykuda2.wrappers.sync_wrappers.accounts import Account
from tests.mocked_api_call_testcase import MockedAPICallTestCase, CredentialMixin


class MockedAccountTesCase(MockedAPICallTestCase):
    def test_can_create_virtual_account(self):
        ...

    def test_can_update_virtual_account(self):
        ...

    def test_can_get_virtual_accounts(self):
        ...

    def test_can_get_virtual_account(self):
        ...

    def test_can_disable_virtual_account(self):
        ...

    def test_can_enable_virtual_account(self):
        ...

    def test_can_get_admin_account_balance(self):
        ...

    def test_can_get_virtual_account_balance(self):
        ...


class AccountTesCase(CredentialMixin, TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()
        cls.wrapper = Account(email=cls.email, api_key=cls.api_key)

    def test_can_create_virtual_account(self):
        response = self.wrapper.create_virtual_account(
            email="johndoe@example.com",
            phone_number="09059438568",
            last_name="Doe",
            first_name="John",
            middle_name="",
            business_name="",
            tracking_reference="qwerty",
        )
        print(response)

    def test_can_update_virtual_account(self):
        ...

    def test_can_get_virtual_accounts(self):
        ...

    def test_can_get_virtual_account(self):
        ...

    def test_can_disable_virtual_account(self):
        ...

    def test_can_enable_virtual_account(self):
        ...

    def test_can_get_admin_account_balance(self):
        ...

    def test_can_get_virtual_account_balance(self):
        ...
