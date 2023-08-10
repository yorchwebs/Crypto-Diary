# This is my basic module to connect MySQL and Flask with:
# peewee, pymysql and python-decouple.

import peewee

from decouple import config

database = peewee.MySQLDatabase(database=config('DB_MYSQL'),
                                host='localhost',
                                user=config('USER_MYSQL'),
                                password=config('PASSWORD_MYSQL'))