import requests
from unittest import TestCase
from unittest.mock import patch

from website import check_website


class TestWebsiteChecker(TestCase):

    def setUp(self) -> None:
        self.url = "https://www.digikala.com"

    def test_check_website_success(self):
        response_mock = {
            "status_code": 200,
            "text": "Example Domain",
        }

        with patch('requests.get') as mock_get:

            mock_get.return_value.text = response_mock["text"]
            mock_get.return_value.status_code = response_mock["status_code"]

            result = check_website(website_url=self.url)
            self.assertIsNotNone(result)
            self.assertIn("pattern_found", result)
            self.assertEqual(result["website_url"], self.url)
            self.assertEqual(
                result["status_code"],
                response_mock["status_code"]
            )

    def test_check_website_timeout(self):
        with patch('requests.get') as mock_get:
            mock_get.side_effect = requests.exceptions.Timeout

            result = check_website(self.url)
            self.assertIsNone(result)

    def test_check_website_connection_error(self):
        with patch('requests.get') as mock_get:
            mock_get.side_effect = requests.exceptions.ConnectionError

            result = check_website(self.url)
            self.assertIsNone(result)

    def test_check_website_request_exception(self):

        with patch('requests.get') as mock_get:
            mock_get.side_effect = requests.exceptions.RequestException

            result = check_website(self.url)
            self.assertIsNone(result)
