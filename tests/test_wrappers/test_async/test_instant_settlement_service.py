from unittest import IsolatedAsyncioTestCase

from pykuda2 import Mode
from pykuda2.wrappers.async_wrappers.instant_settlement_service import (
    AsyncInstantSettlementService,
)
from tests.mocked_api_call_testcase import MockedAsyncAPICallTestCase, CredentialMixin


class MockedAsyncInstantSettlementServiceTestCase(MockedAsyncAPICallTestCase):
    @classmethod
    def setUpClass(cls) -> None:
        # TODO: Requires partnership credentials to really work
        super().setUpClass()
        cls.wrapper = AsyncInstantSettlementService(
            secret_key="invalid-secret", client_password="invalid-password"
        )

    def test_base_url(self):
        self.assertEqual(self.wrapper._base_url, "https://partners-uat.kudabank.com")
        self.wrapper._mode = Mode.PRODUCTION
        self.assertEqual(self.wrapper._base_url, "https://partners.kuda.com")

    async def test_token(self):
        ...

    async def test_headers(self):
        ...

    async def test_can_create_terminal(self):
        ...

    async def test_can_update_terminal(self):
        ...

    async def test_can_all(self):
        ...

    async def test_can_get_settlement_status(self):
        ...

    async def test_can_log_transaction(self):
        ...

    async def test_can_transactions(self):
        ...


class AsyncInstantSettlementServiceTestCase(CredentialMixin, IsolatedAsyncioTestCase):
    @classmethod
    def setUpClass(cls) -> None:
        # TODO: Requires partnership credentials to really work
        super().setUpClass()
        cls.wrapper = AsyncInstantSettlementService(
            secret_key="invalid-secret", client_password="invalid-password"
        )

    async def test_can_create_terminal(self):
        ...

    async def test_can_update_terminal(self):
        ...

    async def test_can_all(self):
        ...

    async def test_can_get_settlement_status(self):
        ...

    async def test_can_log_transaction(self):
        ...

    async def test_can_transactions(self):
        ...
