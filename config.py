from decouple import config

class Config:
    SECRET_KEY = config('SECRET_KEY')
    CRYPTOCOMPARE_API_KEY = config("CRYPTO_COMPARE_KEY")

class DevelopmentConfig(Config):
    DEBUG = True


config = {
    'development': DevelopmentConfig,
    'default': DevelopmentConfig,
}
