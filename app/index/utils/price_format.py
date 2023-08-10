def price_formatter(func):
    def wrapper(*args, **kwargs):
        price = func(*args, **kwargs)
        price_formatter = "{:,.2f}".format(price)
        return price_formatter
    return wrapper