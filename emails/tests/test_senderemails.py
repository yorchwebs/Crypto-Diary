import unittest

from emails.emails import SenderEmail


class TestSenderEmails(unittest.TestCase):
    def setUp(self):
        self.sender_email = SenderEmail()

    def test_generate_message(self):
        self.assertIsInstance(self.sender_email.generate_message(), str)

    def test_email_body_and_connection(self):
        self.assertIsNone(
            self.sender_email.email_body_and_connection(self.sender_email.emails[0])
        )

    def test_send_emails(self):
        self.assertIsNone(self.sender_email.send_emails())

    def tearDown(self):
        del self.sender_email
