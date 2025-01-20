"""This is my Singleton Class to connect MySQL and Flask with:
peewee, pymysql and python-decouple.
"""

import peewee
from decouple import config


class DatabaseSingleton:
    """Singleton class to connect PostgreSQL and Flask with peewee."""

    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.init_db()
        return cls._instance

    def init_db(self):
        """Initialize the database."""
        self.database = peewee.PostgresqlDatabase(
            config("DB_NAME"),
            user=config("DB_USER"),
            password=config("DB_PASSWORD"),
            host=config("DB_HOST"),
            port=config("DB_PORT"),
        )

    def get_database(self):
        """Return the database instance."""
        return self.database
