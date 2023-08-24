import unittest

from config import config

from app import create_app

from emails.emails import SenderEmail

send_email = SenderEmail().email_body_and_connection


class TestCryptoPrices(unittest.TestCase):
    def setUp(self):
        environment = config["testing"]
        self.app = create_app(environment)
        self.client = self.app.test_client()

        self.path = "http://127.0.0.1:5000/"

    def tearDown(self):
        pass

    def test_get_index_page(self):
        response = self.client.get(path=self.path)
        self.assertEqual(response.status_code, 200)

