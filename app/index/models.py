import peewee

from app.db.database import database


class BaseModel(peewee.Model):
    class Meta:
        database = database


class Newsletter(BaseModel):
    name = peewee.CharField(max_length=255)
    email = peewee.CharField(max_length=255, unique=True)

    class Meta:
        table_name = "newsletter_subscribers"
