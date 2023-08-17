from decouple import config

class Config:
    SECRET_KEY = config('SECRET_KEY')
    CRYPTOCOMPARE_API_KEY = config("CRYPTO_COMPARE_KEY")
    MAIL_SERVER = config("MAIL_SERVER")
    MAIL_PORT = config("MAIL_PORT")
    MAIL_USE_TLS = config("MAIL_USE_TLS")
    MAIL_USERNAME = config("MAIL_USERNAME")
    MAIL_PASSWORD = config("MAIL_PASSWORD")
    MAIL_DEFAULT_SENDER = config("MAIL_DEFAULT_SENDER")

class DevelopmentConfig(Config):
    DEBUG = True


config = {
    'development': DevelopmentConfig,
    'default': DevelopmentConfig
}
