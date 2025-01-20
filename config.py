from decouple import config


class Config:
    """
    A configuration class for the Flask application.

    Attributes:
        SECRET_KEY (str): A secret key used by Flask to encrypt session data.
        CRYPTOCOMPARE_API_KEY (str): An API key for the CryptoCompare API.
    """

    SECRET_KEY = config("SECRET_KEY")
    CRYPTOCOMPARE_API_KEY = config("CRYPTO_COMPARE_KEY")


class DevelopmentConfig(Config):
    """
    A configuration class for the Flask application in development mode.

    Attributes:
        DEBUG (bool): Whether or not to enable debug mode.
    """

    DEBUG: bool = True


class TestConfig(Config):
    """
    A configuration class for the Test application in development mode.

    Attributes:
        DEBUG (bool): Whether or not to enable debug mode.
    """

    DEBUG: bool = False


config = {
    "development": DevelopmentConfig,
    "default": DevelopmentConfig,
    "testing": TestConfig,
}
