import time
import cryptocompare

from typing import List
from app.index.utils.price_format import price_formatter

from concurrent.futures import ThreadPoolExecutor

start = time.time()


class CryptoPrices:
    def __init__(self, coins: dict = None, names: dict = None):
        self.coins = cryptocompare.get_price(
            ["BTC", "ETH", "LTC", "BCH", "XRP", "BSV", "EOS", "XLM", "ADA", "TRX"],
            ["USD", "MXN"],
        )

    def get_prices(self) -> dict:
        symbol_list: List[str] = [
            "BTC",
            "ETH",
            "USDT",
            "USDC",
            "BNB",
            "XRP",
            "BUSD",
            "ADA",
            "SOL",
            "DOGE",
        ]
        name_list: List[str] = [
            "Bitcoin",
            "Ethereum",
            "Tether",
            "USD Coin",
            "Binance Coin",
            "XRP",
            "Binance USD",
            "Cardano",
            "Solana",
            "Dogecoin",
        ]
        usd_price_list: List[float] = []
        mxn_price_list: List[float] = []

        while True:
            with ThreadPoolExecutor(max_workers=4) as executor:
                for coin in self.coins:
                    executor.submit(
                        usd_price_list.append(getting_price(self.coins[coin]["USD"]))
                    )
                    executor.submit(
                        mxn_price_list.append(getting_price(self.coins[coin]["MXN"]))
                    )

            break

        return {
            "symbol_list": symbol_list,
            "name_list": name_list,
            "usd_price_list": usd_price_list,
            "mxn_price_list": mxn_price_list,
        }


print(time.time() - start)


@price_formatter
def getting_price(price):
    return price
