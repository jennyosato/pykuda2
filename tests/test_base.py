from unittest import TestCase

from pykuda2.base import APIWrapper, ServiceType, APIResponse, AsyncAPIWrapper
from tests.mocked_api_call_testcase import (
    MockedAPICallTestCase,
    MockedAsyncAPICallTestCase,
)
from httpx import codes as HTTP_STATUS_CODE


class APIWrapperTestCase(MockedAPICallTestCase):
    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()
        cls.wrapper = APIWrapper(email=cls.email, api_key=cls.api_key)

    def test_token(self):
        self.assertEqual(self.wrapper.token, self.mocked_api_response.text)

    def test_headers(self):
        self.assertDictEqual(
            self.wrapper.headers,
            {
                "authorization": f"Bearer {self.mocked_api_response.text}",
                **self.wrapper.base_headers,
            },
        )

    def test_api_call(self):
        response = self.wrapper.api_call(
            service_type=ServiceType.ADMIN_CREATE_VIRTUAL_ACCOUNT, data={}
        )
        self.assertIsInstance(response, APIResponse)
        self.assertEqual(
            response,
            APIResponse(
                status_code=HTTP_STATUS_CODE.OK,
                status="successful",
                message="This is a mocked response. No real API call to Kuda servers was made.",
                data={"isValid": True},
                raw={
                    "status": "successful",
                    "message": "This is a mocked response. No real API call to Kuda servers was made.",
                    "data": {"isValid": True},
                },
            ),
        )


class AsyncAPIWrapperTestCase(MockedAsyncAPICallTestCase):
    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()
        cls.wrapper = AsyncAPIWrapper(email=cls.email, api_key=cls.api_key)

    async def test_token(self):
        self.assertEqual(await self.wrapper.token, self.mocked_api_response.text)

    async def test_headers(self):
        self.assertDictEqual(
            await self.wrapper.headers,
            {
                "authorization": f"Bearer {self.mocked_api_response.text}",
                **self.wrapper.base_headers,
            },
        )

    async def test_api_call(self):
        response = await self.wrapper.api_call(
            service_type=ServiceType.ADMIN_CREATE_VIRTUAL_ACCOUNT, data={}
        )
        self.assertIsInstance(response, APIResponse)
        self.assertEqual(
            response,
            APIResponse(
                status_code=HTTP_STATUS_CODE.OK,
                status="successful",
                message="This is a mocked response. No real API call to Kuda servers was made.",
                data={"isValid": True},
                raw={
                    "status": "successful",
                    "message": "This is a mocked response. No real API call to Kuda servers was made.",
                    "data": {"isValid": True},
                },
            ),
        )
