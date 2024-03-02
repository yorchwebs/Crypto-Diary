"""This is the test file for the application."""

import unittest

from config import config

from app import create_app


class TestCryptoPrices(unittest.TestCase):
    def setUp(self):
        environment: bool = config["testing"]
        self.app = create_app(environment)
        self.client = self.app.test_client()

        self.path = "http://127.0.0.1:5000/"

    def tearDown(self):
        pass

    def test_get_index_page(self):
        response: str = self.client.get(path=self.path)
        self.assertEqual(response.status_code, 200)
