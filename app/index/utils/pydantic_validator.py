"""Pydantic models for validating data."""

from pydantic import BaseModel


class NewsletterSubscriberValidateDataModel(BaseModel):
    """A Pydantic model for newsletter subscription data.

    Attributes:
        email (str): The email address of the subscriber.
    """

    email: str
