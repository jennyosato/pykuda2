from unittest import IsolatedAsyncioTestCase

from pykuda2.wrappers.async_wrappers.accounts import AsyncAccount
from tests.mocked_api_call_testcase import MockedAsyncAPICallTestCase, CredentialMixin


class MockedAsyncAccountTesCase(MockedAsyncAPICallTestCase):
    async def test_can_create_virtual_account(self):
        ...

    async def test_can_update_virtual_account(self):
        ...

    async def test_can_get_virtual_accounts(self):
        ...

    async def test_can_get_virtual_account(self):
        ...

    async def test_can_disable_virtual_account(self):
        ...

    async def test_can_enable_virtual_account(self):
        ...

    async def test_can_get_admin_account_balance(self):
        ...

    async def test_can_get_virtual_account_balance(self):
        ...


class AsyncAccountTesCase(CredentialMixin, IsolatedAsyncioTestCase):
    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()
        cls.wrapper = AsyncAccount(email=cls.email, api_key=cls.api_key)

    async def test_can_create_virtual_account(self):
        response = await self.wrapper.create_virtual_account(
            email="johndoe@example.com",
            phone_number="09059438568",
            last_name="Doe",
            first_name="John",
            middle_name="",
            business_name="",
            tracking_reference="qwerty",
        )

    async def test_can_update_virtual_account(self):
        ...

    async def test_can_get_virtual_accounts(self):
        ...

    async def test_can_get_virtual_account(self):
        ...

    async def test_can_disable_virtual_account(self):
        ...

    async def test_can_enable_virtual_account(self):
        ...

    async def test_can_get_admin_account_balance(self):
        ...

    async def test_can_get_virtual_account_balance(self):
        ...
