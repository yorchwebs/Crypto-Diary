""" This is the entry point of the application. """

from app import create_app
from config import config


config_name = config["development"]
app = create_app(config_name)


if __name__ == "__main__":
    app.run()
