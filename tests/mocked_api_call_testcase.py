import os
from unittest import TestCase, IsolatedAsyncioTestCase
from unittest.mock import Mock, patch

from dotenv import load_dotenv


class TestDummyData:
    @classmethod
    def setUpClass(cls) -> None:
        cls.email = "test-email@exampl.com"
        cls.api_key = "do9fr983hri8d4e"
        cls.mocked_api_response = Mock(spec="httpx.Response")
        cls.mocked_api_response.status_code = 200
        cls.mocked_api_response.text = (
            "ey.JefilwuhDFLKJHG8Y9IFLKJDSNF98879YJKFB8FKK"
            "JHHSdasfdnslfkjnIlnlKFJ&47kellCFKljfkdjbndksjds"
        )
        cls.mocked_api_response.json = Mock()
        cls.mocked_api_response.json.return_value = {
            "status": "successful",
            "message": "This is a mocked response. No real API call to Kuda servers was made.",
            "data": {"isValid": True},
        }


class MockedAPICallTestCase(TestDummyData, TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()
        get_patcher = patch("httpx.get")
        post_patcher = patch("httpx.post")
        put_patcher = patch("httpx.put")
        patch_patcher = patch("httpx.patch")
        delete_patcher = patch("httpx.delete")
        options_patcher = patch("httpx.options")
        head_patcher = patch("httpx.head")

        mock_get = get_patcher.start()
        mock_get.return_value = cls.mocked_api_response

        mock_post = post_patcher.start()
        mock_post.return_value = cls.mocked_api_response

        mock_put = put_patcher.start()
        mock_put.return_value = cls.mocked_api_response

        mock_patch = patch_patcher.start()
        mock_patch.return_value = cls.mocked_api_response

        mock_delete = delete_patcher.start()
        mock_delete.return_value = cls.mocked_api_response

        mock_options = options_patcher.start()
        mock_options.return_value = cls.mocked_api_response

        mock_head = head_patcher.start()
        mock_head.return_value = cls.mocked_api_response


class MockedAsyncAPICallTestCase(TestDummyData, IsolatedAsyncioTestCase):
    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()
        get_patcher = patch("httpx._client.AsyncClient.get")
        post_patcher = patch("httpx._client.AsyncClient.post")
        put_patcher = patch("httpx._client.AsyncClient.put")
        patch_patcher = patch("httpx._client.AsyncClient.patch")
        delete_patcher = patch("httpx._client.AsyncClient.delete")
        options_patcher = patch("httpx._client.AsyncClient.options")
        head_patcher = patch("httpx._client.AsyncClient.head")

        mock_get = get_patcher.start()
        mock_get.return_value = cls.mocked_api_response

        mock_post = post_patcher.start()
        mock_post.return_value = cls.mocked_api_response

        mock_put = put_patcher.start()
        mock_put.return_value = cls.mocked_api_response

        mock_patch = patch_patcher.start()
        mock_patch.return_value = cls.mocked_api_response

        mock_delete = delete_patcher.start()
        mock_delete.return_value = cls.mocked_api_response

        mock_options = options_patcher.start()
        mock_options.return_value = cls.mocked_api_response

        mock_head = head_patcher.start()
        mock_head.return_value = cls.mocked_api_response


class CredentialMixin:
    @classmethod
    def setUpClass(cls) -> None:
        load_dotenv()
        cls.email = os.getenv("KUDA_EMAIL_ADDRESS")
        cls.api_key = os.getenv("KUDA_API_KEY")
