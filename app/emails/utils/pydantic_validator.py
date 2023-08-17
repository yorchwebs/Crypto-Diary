from pydantic import BaseModel


class NewsletterModel(BaseModel):
    name: str
    email: str
