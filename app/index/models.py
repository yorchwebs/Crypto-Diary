""" This file contains the models for the index app. """

import peewee

from app.db.database import MySQLDatabaseSingleton


database = MySQLDatabaseSingleton().database

class BaseModel(peewee.Model):
    """
    A base model class that all other models should inherit from.

    Attributes:
        database (Database): The database connection to use for this model.
    """
    class Meta:
        database = database


class NewsletterSubscriber(BaseModel):
    """
    A base model class that all other models should inherit from.

    Attributes:
        id (AutoField): A unique identifier for the model.
        created_at (DateTimeField): The date and time when the model was created.
        updated_at (DateTimeField): The date and time when the model was last updated.
    """
    email = peewee.CharField(max_length=255, unique=True)
    created_at = peewee.DateTimeField(default=peewee.datetime.datetime.now)

    class Meta:
        table_name = "newsletter_subscribers"
