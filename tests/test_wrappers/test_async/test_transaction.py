from unittest import IsolatedAsyncioTestCase

from pykuda2 import TransferInstruction, TransactionStatus
from pykuda2.wrappers.async_wrappers.transaction import AsyncTransaction
from tests.mocked_api_call_testcase import MockedAsyncAPICallTestCase, CredentialMixin
from httpx import codes as HTTP_STATUS_CODE


class MockedAsyncTransactionTestCase(MockedAsyncAPICallTestCase):
    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()
        cls.wrapper = AsyncTransaction(email=cls.email, api_key=cls.api_key)

    async def test_can_get_banks(self):
        response = await self.wrapper.get_banks()
        self.assertEqual(response.status_code, HTTP_STATUS_CODE.OK)
        self.assertTrue(response.status)

    async def test_can_confirm_transfer_recipient(self):
        response = await self.wrapper.confirm_transfer_recipient(
            beneficiary_account_number="2504201301",
            beneficiary_bank_code="999129",
            sender_tracking_reference="qwerty",
            is_request_from_virtual_account=False,
        )
        self.assertEqual(response.status_code, HTTP_STATUS_CODE.OK)
        self.assertTrue(response.status)

    async def test_can_fund_transfer(self):
        # TODO: Test properly
        response = await self.wrapper.fund_transfer(
            beneficiary_bank_code="999129",
            beneficiary_name="John Doe",
            amount=5000,
            beneficiary_account="2504201301",
            narration="Test transfer",
            sender_name="Coyote Solutions",
            name_enquiry_session_id="",
            client_account_number="3000606742",
        )
        self.assertEqual(response.status_code, HTTP_STATUS_CODE.OK)

    async def test_can_virtual_account_fund_transfer(self):
        response = await self.wrapper.virtual_account_fund_transfer(
            tracking_reference="qwerty",
            beneficiary_bank_code="999129",
            beneficiary_name="John Doe",
            amount=5000,
            beneficiary_account="2504201442",
            narration="Test transfer",
            sender_name="Coyote Solutions",
            name_enquiry_id="",
            client_account_number="3000606742",
        )
        self.assertEqual(response.status_code, HTTP_STATUS_CODE.OK)

    async def test_can_process_transfers(self):
        response = await self.wrapper.process_transfers(
            fund_transfer_instructions=[
                TransferInstruction(
                    account_number="2504201301",
                    account_name="(Coyote IT)-Doe John",
                    beneficiary_bank_code="999129",
                    amount=5000,
                    bank_code="999129",
                    narration="Test transaction",
                    bank_name="Kuda",
                    long_code="",
                    reference="azerty",
                )
            ]
        )
        self.assertEqual(response.status_code, HTTP_STATUS_CODE.OK)
        self.assertTrue(response.status)

    async def test_can_get_transfer_instructions(self):
        response = await self.wrapper.get_transfer_instructions(
            account_number="2504201301",
            reference="azerty",
            amount=5000,
            original_request_ref="",
            status=TransactionStatus.PENDING,
            page_number=1,
            page_size=50,
        )
        self.assertEqual(response.status_code, HTTP_STATUS_CODE.OK)
        self.assertTrue(response.status)

    async def test_can_get_transaction_logs(self):
        response = await self.wrapper.get_transaction_logs(
            response_reference="",
            request_reference="",
            transaction_date="2023-04-28",
            has_transaction_date_range_filter=False,
            start_date="",
            end_date="",
            page_size=50,
            page_number=1,
        )
        self.assertEqual(response.status_code, HTTP_STATUS_CODE.OK)

    async def test_can_get_transaction_history(self):
        response = await self.wrapper.get_transaction_history(
            page_number=1, page_size=50
        )
        self.assertEqual(response.status_code, HTTP_STATUS_CODE.OK)
        self.assertTrue(response.status)

    async def test_can_get_filtered_transaction_history(self):
        response = await self.wrapper.get_filtered_transaction_history(
            page_size=5, page_number=1, start_date="2023-04-27", end_date="2023-04-29"
        )
        self.assertEqual(response.status_code, HTTP_STATUS_CODE.OK)
        self.assertTrue(response.status)

    async def test_can_get_virtual_account_transaction_history(self):
        response = await self.wrapper.get_virtual_account_transaction_history(
            tracking_reference="qwerty", page_size=5, page_number=1
        )
        self.assertEqual(response.status_code, HTTP_STATUS_CODE.OK)
        self.assertTrue(response.status)

    async def test_can_get_virtual_account_filtered_transaction_history(self):
        response = await self.wrapper.get_virtual_account_filtered_transaction_history(
            tracking_reference="qwerty",
            page_size=5,
            page_number=1,
            start_date="2023-04-27",
            end_date="2023-04-29",
        )
        self.assertEqual(response.status_code, HTTP_STATUS_CODE.OK)
        self.assertTrue(response.status)

    async def test_can_get_status(self):
        response = await self.wrapper.get_status(
            is_third_party_bank_transfer=False, transaction_request_reference="dkskkw"
        )
        self.assertEqual(response.status_code, HTTP_STATUS_CODE.OK)

    async def test_can_fund_virtual_account(self):
        response = await self.wrapper.fund_virtual_account(
            tracking_reference="qwerty", amount=5500, narration="Test credit"
        )
        self.assertEqual(response.status_code, HTTP_STATUS_CODE.OK)

    async def test_can_withdraw_from_virtual_account(self):
        response = await self.wrapper.withdraw_from_virtual_account(
            tracking_reference="qwerty", amount=3000, narration="Test debit"
        )
        self.assertEqual(response.status_code, HTTP_STATUS_CODE.OK)


class AsyncTransactionTestCase(CredentialMixin, IsolatedAsyncioTestCase):
    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()
        cls.wrapper = AsyncTransaction(email=cls.email, api_key=cls.api_key)

    async def test_can_get_banks(self):
        response = await self.wrapper.get_banks()
        self.assertEqual(response.status_code, HTTP_STATUS_CODE.OK)
        self.assertTrue(response.status)

    async def test_can_confirm_transfer_recipient(self):
        response = await self.wrapper.confirm_transfer_recipient(
            beneficiary_account_number="2504201301",
            beneficiary_bank_code="999129",
            sender_tracking_reference="qwerty",
            is_request_from_virtual_account=False,
        )
        self.assertEqual(response.status_code, HTTP_STATUS_CODE.OK)
        self.assertTrue(response.status)

    async def test_can_fund_transfer(self):
        # TODO: Test properly
        response = await self.wrapper.fund_transfer(
            beneficiary_bank_code="999129",
            beneficiary_name="John Doe",
            amount=5000,
            beneficiary_account="2504201301",
            narration="Test transfer",
            sender_name="Coyote Solutions",
            name_enquiry_session_id="",
            client_account_number="3000606742",
        )
        self.assertEqual(response.status_code, HTTP_STATUS_CODE.OK)

    async def test_can_virtual_account_fund_transfer(self):
        response = await self.wrapper.virtual_account_fund_transfer(
            tracking_reference="qwerty",
            beneficiary_bank_code="999129",
            beneficiary_name="John Doe",
            amount=5000,
            beneficiary_account="2504201442",
            narration="Test transfer",
            sender_name="Coyote Solutions",
            name_enquiry_id="",
            client_account_number="3000606742",
        )
        self.assertEqual(response.status_code, HTTP_STATUS_CODE.OK)

    async def test_can_process_transfers(self):
        response = await self.wrapper.process_transfers(
            fund_transfer_instructions=[
                TransferInstruction(
                    account_number="2504201301",
                    account_name="(Coyote IT)-Doe John",
                    beneficiary_bank_code="999129",
                    amount=5000,
                    bank_code="999129",
                    narration="Test transaction",
                    bank_name="Kuda",
                    long_code="",
                    reference="azerty",
                )
            ]
        )
        self.assertEqual(response.status_code, HTTP_STATUS_CODE.OK)
        self.assertTrue(response.status)

    async def test_can_get_transfer_instructions(self):
        response = await self.wrapper.get_transfer_instructions(
            account_number="2504201301",
            reference="azerty",
            amount=5000,
            original_request_ref="",
            status=TransactionStatus.PENDING,
            page_number=1,
            page_size=50,
        )
        self.assertEqual(response.status_code, HTTP_STATUS_CODE.OK)
        self.assertTrue(response.status)

    async def test_can_get_transaction_logs(self):
        response = await self.wrapper.get_transaction_logs(
            response_reference="",
            request_reference="",
            transaction_date="2023-04-28",
            has_transaction_date_range_filter=False,
            start_date="",
            end_date="",
            page_size=50,
            page_number=1,
        )
        self.assertEqual(response.status_code, HTTP_STATUS_CODE.OK)

    async def test_can_get_transaction_history(self):
        response = await self.wrapper.get_transaction_history(
            page_number=1, page_size=50
        )
        self.assertEqual(response.status_code, HTTP_STATUS_CODE.OK)
        self.assertTrue(response.status)

    async def test_can_get_filtered_transaction_history(self):
        response = await self.wrapper.get_filtered_transaction_history(
            page_size=5, page_number=1, start_date="2023-04-27", end_date="2023-04-29"
        )
        self.assertEqual(response.status_code, HTTP_STATUS_CODE.OK)
        self.assertTrue(response.status)

    async def test_can_get_virtual_account_transaction_history(self):
        response = await self.wrapper.get_virtual_account_transaction_history(
            tracking_reference="qwerty", page_size=5, page_number=1
        )
        self.assertEqual(response.status_code, HTTP_STATUS_CODE.OK)
        self.assertTrue(response.status)

    async def test_can_get_virtual_account_filtered_transaction_history(self):
        response = await self.wrapper.get_virtual_account_filtered_transaction_history(
            tracking_reference="qwerty",
            page_size=5,
            page_number=1,
            start_date="2023-04-27",
            end_date="2023-04-29",
        )
        self.assertEqual(response.status_code, HTTP_STATUS_CODE.OK)
        self.assertTrue(response.status)

    async def test_can_get_status(self):
        response = await self.wrapper.get_status(
            is_third_party_bank_transfer=False, transaction_request_reference="dkskkw"
        )
        self.assertEqual(response.status_code, HTTP_STATUS_CODE.OK)

    async def test_can_fund_virtual_account(self):
        response = await self.wrapper.fund_virtual_account(
            tracking_reference="qwerty", amount=5500, narration="Test credit"
        )
        self.assertEqual(response.status_code, HTTP_STATUS_CODE.OK)

    async def test_can_withdraw_from_virtual_account(self):
        response = await self.wrapper.withdraw_from_virtual_account(
            tracking_reference="qwerty", amount=3000, narration="Test debit"
        )
        self.assertEqual(response.status_code, HTTP_STATUS_CODE.OK)
