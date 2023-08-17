import cryptocompare

from typing import List

from concurrent.futures import ThreadPoolExecutor

from app.index.utils.price_format import price_formatter


class CryptoPrice:
    def __init__(self):
        self.coins = cryptocompare.get_price(
            ["BTC", "ETH", "USDT", "USDC", "BNB", "XRP", "BUSD", "ADA", "SOL", "DOGE"],
            ["USD", "MXN"],
        )

    @property
    def prices(self) -> dict:
        SYMBOL_LIST: List[str] = [
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
        NAME_LIST: List[str] = [
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

        with ThreadPoolExecutor(max_workers=4) as executor:
            for coin in self.coins:
                executor.submit(
                    usd_price_list.append(getting_price(self.coins[coin]["USD"]))
                )
                executor.submit(
                    mxn_price_list.append(getting_price(self.coins[coin]["MXN"]))
                )

        data_to_return = {
            "symbol_list": SYMBOL_LIST,
            "name_list": NAME_LIST,
            "usd_price_list": usd_price_list,
            "mxn_price_list": mxn_price_list,
        }

        return data_to_return



@price_formatter
def getting_price(price):
    return price
