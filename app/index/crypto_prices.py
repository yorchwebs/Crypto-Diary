"""This is a docstring for the `CryptoPrice`."""

import cryptocompare

from typing import List

from concurrent.futures import ThreadPoolExecutor

from app.index.utils.price_format import getting_price


class CryptoPrice:
    """A class to represent the current prices of popular cryptocurrencies.

    Attributes
    ----------
    coins : dict
        A dictionary containing the current prices of popular cryptocurrencies
        in USD and MXN.

    Methods
    -------
    __init__() -> None:
        Initializes the CryptoPrice object and retrieves the current prices of
        popular cryptocurrencies.
    prices() -> dict:
        Returns a dictionary with the current prices of cryptocurrencies
        in USD and MXN.
    """

    def __init__(self) -> None:
        """Initializes a CryptoPrice object and retrieves the current prices
        of popular cryptocurrencies.

        Attributes
        ----------
        coins : dict
            A dictionary containing the current prices of popular
            cryptocurrencies in USD and MXN.
        """

        self.coins = cryptocompare.get_price(
            [
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
            ],
            ["USD", "MXN"],
        )

    @property
    def prices(self) -> dict:
        """Returns a dic. with the current prices of cryptocurrencies in
        USD and MXN.

        This method uses the `getting_price` function to get the current
        prices of each cryptocurrency in USD and MXN. It does this by sending
        a separate thread for Each cryptocurrency to the `threadpoolexecutor`
        with a max. of 4 worker threads. The resulting prices are stored in
        two separate lists, `USD_PRICE_LIST` and `mxn_price_list`,
        which are then combined with the `Symbol_List` and The lists of
        `name_list` to form the final dictionary.

        :args: None

        :return:
            A dictionary with the following keys:
            - "Symbol_list": a list of strings with the symbols of each
                            cryptocurrency.
            - "name_list": a list of strings with the names of each
                            cryptocurrency.
            - "USD_PRICE_LIST": a list of floats with the current prices
                of each cryptocurrency in USD.
            - "mxn_price_list": a list of floats with the current prices
                of each cryptocurrency in mxn.
        """
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
        with ThreadPoolExecutor(max_workers=4) as executor:
            usd_price_list: List[float] = [
                executor.submit(
                    getting_price, self.coins[coin]["USD"]
                ).result()  # noqa
                for coin in self.coins
            ]
            mxn_price_list: List[float] = [
                executor.submit(
                    getting_price, self.coins[coin]["MXN"]
                ).result()  # noqa
                for coin in self.coins
            ]

        data_to_return: dict = {
            "symbol_list": SYMBOL_LIST,
            "name_list": NAME_LIST,
            "usd_price_list": usd_price_list,
            "mxn_price_list": mxn_price_list,
        }

        return data_to_return
