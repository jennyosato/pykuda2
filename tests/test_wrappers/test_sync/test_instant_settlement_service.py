from unittest import TestCase

from pykuda2 import Mode
from pykuda2.wrappers.sync_wrappers.instant_settlement_service import (
    InstantSettlementService,
)
from tests.mocked_api_call_testcase import MockedAPICallTestCase


class MockedInstantSettlementServiceTestCase(MockedAPICallTestCase):
    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()
        cls.wrapper = InstantSettlementService(
            secret_key="invalid-secret", client_password="invalid-password"
        )

    def test_base_url(self):
        self.assertEqual(self.wrapper.base_url, "https://partners-uat.kudabank.com")
        self.wrapper.mode = Mode.PRODUCTION
        self.assertEqual(self.wrapper.base_url, "https://partners.kuda.com")

    def test_token(self):
        ...

    def test_headers(self):
        ...

    def test_can_create_terminal(self):
        ...

    def test_can_update_terminal(self):
        ...

    def test_can_all(self):
        ...

    def test_can_get_settlement_status(self):
        ...

    def test_can_log_transaction(self):
        ...

    def test_can_transactions(self):
        ...


class InstantSettlementServiceTestCase(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        # TODO: Requires partnership credentials to really work
        super().setUpClass()
        cls.wrapper = InstantSettlementService(
            secret_key="invalid-secret", client_password="invalid-password"
        )

    def test_can_create_terminal(self):
        ...

    def test_can_update_terminal(self):
        ...

    def test_can_all(self):
        ...

    def test_can_get_settlement_status(self):
        ...

    def test_can_log_transaction(self):
        ...

    def test_can_transactions(self):
        ...
