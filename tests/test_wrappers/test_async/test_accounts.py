from unittest import IsolatedAsyncioTestCase

from pykuda2.utils import generate_number
from pykuda2.wrappers.async_wrappers.accounts import AsyncAccount
from tests.mocked_api_call_testcase import MockedAsyncAPICallTestCase, CredentialMixin

from httpx import codes as HTTP_STATUS_CODE


class MockedAsyncAccountTesCase(MockedAsyncAPICallTestCase):
    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()
        cls.wrapper = AsyncAccount(email=cls.email, api_key=cls.api_key)

    async def test_can_create_virtual_account(self):
        response = await self.wrapper.create_virtual_account(
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

    async def test_can_update_virtual_account(self):
        tracking_reference = str(generate_number(10))
        await self.wrapper.create_virtual_account(
            email=f"johndoe{generate_number(10)}@example.com",
            phone_number=f"070{generate_number(8)}",
            last_name="Doe",
            first_name="John",
            middle_name="",
            business_name="",
            tracking_reference=tracking_reference,
        )
        response = await self.wrapper.update_virtual_account(
            tracking_reference=tracking_reference,
            first_name="Gbenga",
            last_name="Adeyi",
        )
        self.assertEqual(response.status_code, HTTP_STATUS_CODE.OK)
        self.assertTrue(response.status)

    async def test_can_get_virtual_accounts(self):
        response = await self.wrapper.get_virtual_accounts(page_size=50, page_number=1)
        self.assertEqual(response.status_code, HTTP_STATUS_CODE.OK)
        self.assertTrue(response.status)

    async def test_can_get_virtual_account(self):
        response = await self.wrapper.get_virtual_account(tracking_reference="qwerty")
        self.assertEqual(response.status_code, HTTP_STATUS_CODE.OK)
        self.assertTrue(response.status)

    async def test_can_disable_virtual_account(self):
        response = await self.wrapper.disable_virtual_account(
            tracking_reference="9466500772"
        )
        self.assertEqual(response.status_code, HTTP_STATUS_CODE.OK)
        self.assertTrue(response.status)

    async def test_can_enable_virtual_account(self):
        response = await self.wrapper.enable_virtual_account(
            tracking_reference="264977600"
        )
        self.assertEqual(response.status_code, HTTP_STATUS_CODE.OK)
        self.assertTrue(response.status)

    async def test_can_get_admin_account_balance(self):
        response = await self.wrapper.get_admin_account_balance()
        self.assertEqual(response.status_code, HTTP_STATUS_CODE.OK)
        self.assertTrue(response.status)

    async def test_can_get_virtual_account_balance(self):
        response = await self.wrapper.get_virtual_account_balance(
            tracking_reference="264977600"
        )
        self.assertEqual(response.status_code, HTTP_STATUS_CODE.OK)
        self.assertTrue(response.status)


class AsyncAccountTesCase(CredentialMixin, IsolatedAsyncioTestCase):
    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()
        cls.wrapper = AsyncAccount(email=cls.email, api_key=cls.api_key)

    async def test_can_create_virtual_account(self):
        response = await self.wrapper.create_virtual_account(
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

    async def test_can_update_virtual_account(self):
        tracking_reference = str(generate_number(10))
        await self.wrapper.create_virtual_account(
            email=f"johndoe{generate_number(10)}@example.com",
            phone_number=f"070{generate_number(8)}",
            last_name="Doe",
            first_name="John",
            middle_name="",
            business_name="",
            tracking_reference=tracking_reference,
        )
        response = await self.wrapper.update_virtual_account(
            tracking_reference=tracking_reference,
            first_name="Gbenga",
            last_name="Adeyi",
        )
        self.assertEqual(response.status_code, HTTP_STATUS_CODE.OK)
        self.assertTrue(response.status)

    async def test_can_get_virtual_accounts(self):
        response = await self.wrapper.get_virtual_accounts(page_size=50, page_number=1)
        self.assertEqual(response.status_code, HTTP_STATUS_CODE.OK)
        self.assertTrue(response.status)

    async def test_can_get_virtual_account(self):
        response = await self.wrapper.get_virtual_account(tracking_reference="qwerty")
        self.assertEqual(response.status_code, HTTP_STATUS_CODE.OK)
        self.assertTrue(response.status)

    async def test_can_disable_virtual_account(self):
        response = await self.wrapper.disable_virtual_account(
            tracking_reference="9466500772"
        )
        self.assertEqual(response.status_code, HTTP_STATUS_CODE.OK)
        self.assertTrue(response.status)

    async def test_can_enable_virtual_account(self):
        response = await self.wrapper.enable_virtual_account(
            tracking_reference="264977600"
        )
        self.assertEqual(response.status_code, HTTP_STATUS_CODE.OK)
        self.assertTrue(response.status)

    async def test_can_get_admin_account_balance(self):
        response = await self.wrapper.get_admin_account_balance()
        self.assertEqual(response.status_code, HTTP_STATUS_CODE.OK)
        self.assertTrue(response.status)

    async def test_can_get_virtual_account_balance(self):
        response = await self.wrapper.get_virtual_account_balance(
            tracking_reference="264977600"
        )
        self.assertEqual(response.status_code, HTTP_STATUS_CODE.OK)
        self.assertTrue(response.status)
