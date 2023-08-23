import unittest

from app.index.crypto_prices import CryptoPrice


class TestCryptoPricesApp(unittest.TestCase):
    def setUp(self):
        self.crypto_price = CryptoPrice()

    def test_coins(self):
        self.assertIsInstance(self.crypto_price.prices, dict)

    def test_prices(self):
        self.assertIsInstance(self.crypto_price.prices, dict)

    def tearDown(self):
        del self.crypto_price
