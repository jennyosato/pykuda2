from unittest import IsolatedAsyncioTestCase

from httpx import codes as HTTP_STATUS_CODE

from pykuda2 import Gender
from pykuda2.utils import generate_number, CardChannel
from pykuda2.wrappers.async_wrappers.card import AsyncCard
from tests.mocked_api_call_testcase import MockedAsyncAPICallTestCase, CredentialMixin


class MockedAsyncCardTestCase(MockedAsyncAPICallTestCase):
    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()
        cls.wrapper = AsyncCard(email=cls.email, api_key=cls.api_key)

    async def test_can_request_card(self):
        # TODO: Properly test this method.
        response = await self.wrapper.request_card(
            tracking_reference=str(generate_number(10)),
            name_on_card="Gbenga Adeyi",
            country="NIGERIA",
            gender=Gender.MALE,
            additional_phone_number="070123456378",
            delivery_city="Ipaja",
            delivery_lga="Alimosho",
            delivery_landmark="",
            delivery_state="lagos",
            delivery_street_no_and_name="1 Kola ogunjale",
            date_of_birth="1999-04-29",
        )
        self.assertEqual(response.status_code, HTTP_STATUS_CODE.OK)

    async def test_can_get_cards(self):
        # TODO: Properly test this method.
        response = await self.wrapper.get_cards(tracking_reference="qwerty")
        self.assertEqual(response.status_code, HTTP_STATUS_CODE.OK)

    async def test_can_activate_card(self):
        response = await self.wrapper.activate_card(
            pan=123, cvv=123, id=12345, tracking_reference="qwerty"
        )
        self.assertEqual(response.status_code, HTTP_STATUS_CODE.OK)

    async def test_can_deactivate_card(self):
        response = await self.wrapper.deactivate_card(
            id=12345, tracking_reference="qwerty"
        )
        self.assertEqual(response.status_code, HTTP_STATUS_CODE.OK)

    async def test_can_set_card_limit(self):
        response = await self.wrapper.set_card_limit(
            id=12345, tracking_reference="qwerty", channel=CardChannel.ATM, limit=50_000
        )
        self.assertEqual(response.status_code, HTTP_STATUS_CODE.OK)

    async def test_can_manage_card_channel(self):
        response = await self.wrapper.manage_card_channel(
            id=123, tracking_reference="qwerty", channel=CardChannel.POS, limit=50_000
        )
        self.assertEqual(response.status_code, HTTP_STATUS_CODE.OK)

    async def test_can_change_card_pin(self):
        response = await self.wrapper.change_card_pin(
            id=123, tracking_reference="2322", new_pin=3434
        )
        self.assertEqual(response.status_code, HTTP_STATUS_CODE.OK)

    async def test_can_block_card(self):
        response = await self.wrapper.block_card(tracking_reference="qwerty", id=1234)
        self.assertEqual(response.status_code, HTTP_STATUS_CODE.OK)

    async def test_can_unblock_card(self):
        response = await self.wrapper.unblock_card(
            tracking_reference="qwerty", id=12345
        )
        self.assertEqual(response.status_code, HTTP_STATUS_CODE.OK)


class AsyncCardTestCase(CredentialMixin, IsolatedAsyncioTestCase):
    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()
        cls.wrapper = AsyncCard(email=cls.email, api_key=cls.api_key)

    async def test_can_request_card(self):
        # TODO: Properly test this method.
        response = await self.wrapper.request_card(
            tracking_reference=str(generate_number(10)),
            name_on_card="Gbenga Adeyi",
            country="NIGERIA",
            gender=Gender.MALE,
            additional_phone_number="070123456378",
            delivery_city="Ipaja",
            delivery_lga="Alimosho",
            delivery_landmark="",
            delivery_state="lagos",
            delivery_street_no_and_name="1 Kola ogunjale",
            date_of_birth="1999-04-29",
        )
        self.assertEqual(response.status_code, HTTP_STATUS_CODE.OK)

    async def test_can_get_cards(self):
        # TODO: Properly test this method.
        response = await self.wrapper.get_cards(tracking_reference="qwerty")
        self.assertEqual(response.status_code, HTTP_STATUS_CODE.OK)

    async def test_can_activate_card(self):
        response = await self.wrapper.activate_card(
            pan=123, cvv=123, id=12345, tracking_reference="qwerty"
        )
        self.assertEqual(response.status_code, HTTP_STATUS_CODE.OK)

    async def test_can_deactivate_card(self):
        response = await self.wrapper.deactivate_card(
            id=12345, tracking_reference="qwerty"
        )
        self.assertEqual(response.status_code, HTTP_STATUS_CODE.OK)

    async def test_can_set_card_limit(self):
        response = await self.wrapper.set_card_limit(
            id=12345, tracking_reference="qwerty", channel=CardChannel.ATM, limit=50_000
        )
        self.assertEqual(response.status_code, HTTP_STATUS_CODE.OK)

    async def test_can_manage_card_channel(self):
        response = await self.wrapper.manage_card_channel(
            id=123, tracking_reference="qwerty", channel=CardChannel.POS, limit=50_000
        )
        self.assertEqual(response.status_code, HTTP_STATUS_CODE.OK)

    async def test_can_change_card_pin(self):
        response = await self.wrapper.change_card_pin(
            id=123, tracking_reference="2322", new_pin=3434
        )
        self.assertEqual(response.status_code, HTTP_STATUS_CODE.OK)

    async def test_can_block_card(self):
        response = await self.wrapper.block_card(tracking_reference="qwerty", id=1234)
        self.assertEqual(response.status_code, HTTP_STATUS_CODE.OK)

    async def test_can_unblock_card(self):
        response = await self.wrapper.unblock_card(
            tracking_reference="qwerty", id=12345
        )
        self.assertEqual(response.status_code, HTTP_STATUS_CODE.OK)
