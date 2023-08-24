""" Pydantic models for validating data. """

from pydantic import BaseModel


class NewsletterModel(BaseModel):
    """
    A Pydantic model for newsletter subscription data.

    Attributes:
        name (str): The name of the subscriber.
        email (str): The email address of the subscriber.
    """
    email: str
