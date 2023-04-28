from unittest import IsolatedAsyncioTestCase

from httpx import codes as HTTP_STATUS_CODE

from pykuda2 import TransactionType
from pykuda2.wrappers.async_wrappers.savings import AsyncSavings
from tests.mocked_api_call_testcase import MockedAsyncAPICallTestCase, CredentialMixin


class MockedAsyncSavingsTestCase(MockedAsyncAPICallTestCase):
    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()
        cls.wrapper = AsyncSavings(email=cls.email, api_key=cls.api_key)

    async def test_can_create_plain_savings_account(self):
        response = await self.wrapper.create_plain_savings_account(
            name="John Miller", tracking_reference="qwerty"
        )
        self.assertEqual(response.status_code, HTTP_STATUS_CODE.OK)
        self.assertTrue(response.status)

    async def test_can_get_plain_savings_account(self):
        # TODO: Test properly
        response = await self.wrapper.get_plain_savings_account(
            tracking_reference="qwerty", primary_account_number="20000006466301"
        )
        self.assertEqual(response.status_code, HTTP_STATUS_CODE.OK)

    async def test_can_get_plain_savings_accounts(self):
        response = await self.wrapper.get_plain_savings_accounts(
            tracking_reference="qwerty"
        )
        self.assertEqual(response.status_code, HTTP_STATUS_CODE.OK)
        self.assertTrue(response.status)

    async def test_can_credit_or_debit_plain_savings_account(self):
        # TODO: Test properly
        response = await self.wrapper.credit_or_debit_plain_savings_account(
            amount=5000,
            narration="bill",
            transaction_type=TransactionType.CREDIT,
            tracking_reference="qwerty",
        )
        self.assertEqual(response.status_code, HTTP_STATUS_CODE.OK)

    async def test_can_get_plain_savings_account_transactions(self):
        # TODO: Test properly
        response = await self.wrapper.get_plain_savings_account_transactions(
            page_size=10, page_number=1, tracking_reference="qwerty"
        )
        self.assertEqual(response.status_code, HTTP_STATUS_CODE.OK)

    async def test_can_create_open_flexible_savings_account(self):
        # TODO: Test properly
        response = await self.wrapper.create_fixed_savings_account(
            savings_tracking_reference="qwerty",
            name="Test savings",
            virtual_account_tracking_reference="",
            amount=50_000,
            duration="2",
            frequency="DAILY",
            start_now=False,
            start_date="2023-04-29",
            is_interest_earning=True,
        )
        self.assertEqual(response.status_code, HTTP_STATUS_CODE.OK)

    async def test_can_pre_create_open_flexible_savings_account(self):
        response = await self.wrapper.pre_create_open_flexible_savings_account(
            savings_tracking_reference="qwerty",
            name="Test savings",
            virtual_account_tracking_reference="",
            amount=50_000,
            duration="2",
            frequency="DAILY",
            start_now=False,
            start_date="2023-04-29",
            is_interest_earning=True,
        )
        self.assertEqual(response.status_code, HTTP_STATUS_CODE.OK)

    async def test_can_get_open_flexible_savings_account(self):
        # TODO: Test properly.
        response = await self.wrapper.get_open_flexible_savings_account(
            tracking_reference="qwerty", primary_account_number="13244253553"
        )
        self.assertEqual(response.status_code, HTTP_STATUS_CODE.OK)

    async def test_can_get_open_flexible_savings_accounts(self):
        response = await self.wrapper.get_open_flexible_savings_accounts(
            primary_account_number="2343545436", tracking_reference="qwerty"
        )
        self.assertEqual(response.status_code, HTTP_STATUS_CODE.OK)
        self.assertTrue(response.status)

    async def test_can_withdraw_from_flexible_savings_account(self):
        # Test properly.
        response = await self.wrapper.withdrawal_from_flexible_savings_account(
            amount=5000, tracking_reference="qwerty"
        )
        self.assertEqual(response.status_code, HTTP_STATUS_CODE.OK)

    async def test_can_get_flexible_savings_account_transactions(self):
        response = await self.wrapper.get_flexible_savings_account_transactions(
            tracking_reference="qwerty", page_size=50, page_number=1
        )
        self.assertEqual(response.status_code, HTTP_STATUS_CODE.OK)

    async def test_can_create_fixed_savings_account(self):
        # TODO: Test properly.
        response = await self.wrapper.create_fixed_savings_account(
            savings_tracking_reference="qwerty",
            name="Jean Malcom",
            amount=5000,
            duration="5",
            frequency="DAILY",
            start_now=True,
            start_date="",
            is_interest_earning=True,
            virtual_account_tracking_reference="qwerty",
        )
        self.assertEqual(response.status_code, HTTP_STATUS_CODE.OK)

    async def test_can_get_fixed_savings_account(self):
        response = await self.wrapper.get_fixed_savings_account(
            tracking_reference="qwerty"
        )
        self.assertEqual(response.status_code, HTTP_STATUS_CODE.OK)

    async def test_can_get_fixed_savings_accounts(self):
        response = await self.wrapper.get_open_flexible_savings_accounts(
            tracking_reference="qwerty", primary_account_number="132324324"
        )
        self.assertEqual(response.status_code, HTTP_STATUS_CODE.OK)
        self.assertTrue(response.status)

    async def test_can_close_fixed_savings_account(self):
        response = await self.wrapper.close_fixed_savings_account(
            amount=5000, tracking_reference="qwerty"
        )
        self.assertEqual(response.status_code, HTTP_STATUS_CODE.OK)

    async def test_can_get_fixed_savings_account_transactions(self):
        response = await self.wrapper.get_flexible_savings_account_transactions(
            tracking_reference="qwerty", page_size=50, page_number=1
        )
        self.assertEqual(response.status_code, HTTP_STATUS_CODE.OK)


class AsyncSavingsTestCase(CredentialMixin, IsolatedAsyncioTestCase):
    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()
        cls.wrapper = AsyncSavings(email=cls.email, api_key=cls.api_key)

    async def test_can_create_plain_savings_account(self):
        response = await self.wrapper.create_plain_savings_account(
            name="John Miller", tracking_reference="qwerty"
        )
        self.assertEqual(response.status_code, HTTP_STATUS_CODE.OK)
        self.assertTrue(response.status)

    async def test_can_get_plain_savings_account(self):
        # TODO: Test properly
        response = await self.wrapper.get_plain_savings_account(
            tracking_reference="qwerty", primary_account_number="20000006466301"
        )
        self.assertEqual(response.status_code, HTTP_STATUS_CODE.OK)

    async def test_can_get_plain_savings_accounts(self):
        response = await self.wrapper.get_plain_savings_accounts(
            tracking_reference="qwerty"
        )
        self.assertEqual(response.status_code, HTTP_STATUS_CODE.OK)
        self.assertTrue(response.status)

    async def test_can_credit_or_debit_plain_savings_account(self):
        # TODO: Test properly
        response = await self.wrapper.credit_or_debit_plain_savings_account(
            amount=5000,
            narration="bill",
            transaction_type=TransactionType.CREDIT,
            tracking_reference="qwerty",
        )
        self.assertEqual(response.status_code, HTTP_STATUS_CODE.OK)

    async def test_can_get_plain_savings_account_transactions(self):
        # TODO: Test properly
        response = await self.wrapper.get_plain_savings_account_transactions(
            page_size=10, page_number=1, tracking_reference="qwerty"
        )
        self.assertEqual(response.status_code, HTTP_STATUS_CODE.OK)

    async def test_can_create_open_flexible_savings_account(self):
        # TODO: Test properly
        response = await self.wrapper.create_fixed_savings_account(
            savings_tracking_reference="qwerty",
            name="Test savings",
            virtual_account_tracking_reference="",
            amount=50_000,
            duration="2",
            frequency="DAILY",
            start_now=False,
            start_date="2023-04-29",
            is_interest_earning=True,
        )
        self.assertEqual(response.status_code, HTTP_STATUS_CODE.OK)

    async def test_can_pre_create_open_flexible_savings_account(self):
        response = await self.wrapper.pre_create_open_flexible_savings_account(
            savings_tracking_reference="qwerty",
            name="Test savings",
            virtual_account_tracking_reference="",
            amount=50_000,
            duration="2",
            frequency="DAILY",
            start_now=False,
            start_date="2023-04-29",
            is_interest_earning=True,
        )
        self.assertEqual(response.status_code, HTTP_STATUS_CODE.OK)

    async def test_can_get_open_flexible_savings_account(self):
        # TODO: Test properly.
        response = await self.wrapper.get_open_flexible_savings_account(
            tracking_reference="qwerty", primary_account_number="13244253553"
        )
        self.assertEqual(response.status_code, HTTP_STATUS_CODE.OK)

    async def test_can_get_open_flexible_savings_accounts(self):
        response = await self.wrapper.get_open_flexible_savings_accounts(
            primary_account_number="2343545436", tracking_reference="qwerty"
        )
        self.assertEqual(response.status_code, HTTP_STATUS_CODE.OK)
        self.assertTrue(response.status)

    async def test_can_withdraw_from_flexible_savings_account(self):
        # Test properly.
        response = await self.wrapper.withdrawal_from_flexible_savings_account(
            amount=5000, tracking_reference="qwerty"
        )
        self.assertEqual(response.status_code, HTTP_STATUS_CODE.OK)

    async def test_can_get_flexible_savings_account_transactions(self):
        response = await self.wrapper.get_flexible_savings_account_transactions(
            tracking_reference="qwerty", page_size=50, page_number=1
        )
        self.assertEqual(response.status_code, HTTP_STATUS_CODE.OK)

    async def test_can_create_fixed_savings_account(self):
        # TODO: Test properly.
        response = await self.wrapper.create_fixed_savings_account(
            savings_tracking_reference="qwerty",
            name="Jean Malcom",
            amount=5000,
            duration="5",
            frequency="DAILY",
            start_now=True,
            start_date="",
            is_interest_earning=True,
            virtual_account_tracking_reference="qwerty",
        )
        self.assertEqual(response.status_code, HTTP_STATUS_CODE.OK)

    async def test_can_get_fixed_savings_account(self):
        response = await self.wrapper.get_fixed_savings_account(
            tracking_reference="qwerty"
        )
        self.assertEqual(response.status_code, HTTP_STATUS_CODE.OK)

    async def test_can_get_fixed_savings_accounts(self):
        response = await self.wrapper.get_open_flexible_savings_accounts(
            tracking_reference="qwerty", primary_account_number="132324324"
        )
        self.assertEqual(response.status_code, HTTP_STATUS_CODE.OK)
        self.assertTrue(response.status)

    async def test_can_close_fixed_savings_account(self):
        response = await self.wrapper.close_fixed_savings_account(
            amount=5000, tracking_reference="qwerty"
        )
        self.assertEqual(response.status_code, HTTP_STATUS_CODE.OK)

    async def test_can_get_fixed_savings_account_transactions(self):
        response = await self.wrapper.get_flexible_savings_account_transactions(
            tracking_reference="qwerty", page_size=50, page_number=1
        )
        self.assertEqual(response.status_code, HTTP_STATUS_CODE.OK)
