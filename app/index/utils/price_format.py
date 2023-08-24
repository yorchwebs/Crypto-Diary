"""
This module contains a decorator that formats a price value to a string with two.
"""

def price_formatter(func) -> callable:
    """
    A decorator that formats a price value to a string with two decimal places and
    commas as thousands separators.

    Args:
        func (callable): The function to be decorated.

    Returns:
        A wrapper function that formats the price value returned by the decorated
        function.
    """
    def wrapper(*args, **kwargs):
        price: float = func(*args, **kwargs)
        price_formatter: float = "{:,.2f}".format(price)
        return price_formatter
    return wrapper

@price_formatter
def getting_price(price) -> str:
    """
    A function that returns a formatted price value.

    Args:
        price (float): The price value to be formatted.

    Returns:
        A string with the formatted price value, with two decimal places and commas as
        thousands separators.
    """
    return price