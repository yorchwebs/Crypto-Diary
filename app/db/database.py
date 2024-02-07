""" Database connection module. """

import peewee

from decouple import config


class MySQLDatabaseSingleton:
    """A singleton class for creating a MySQL database connection.

    Attributes:
        _instance (MySQLDatabaseSingleton): The singleton instance of the
                                            class.
        database (MySQLDatabase): The MySQL database connection object.
    """
    _instance = None

    def __new__(cls):
        """Creates a new instance of the class if it doesn't exist yet,
        or returns the existing instance.

        Returns:
            The singleton instance of the class.
        """
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.init_db()
        return cls._instance

    def init_db(self):
        """Initializes the MySQL database connection object using the
        configuration settings.
        """
        self.database = peewee.MySQLDatabase(
            database=config("DB_MYSQL"),
            user=config("USER_MYSQL"),
            password=config("PASSWORD_MYSQL"),
            host=config("HOST_MYSQL"),
        )
