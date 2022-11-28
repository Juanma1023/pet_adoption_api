import datetime
import peewee

from app.v1.utils.db import db

class User(peewee.Model):
    name = peewee.CharField()
    last_name = peewee.CharField()
    phone = peewee.CharField()
    email = peewee.CharField(unique=True, index=True)
    address = peewee.CharField()
    created_at = peewee.DateTimeField(default=datetime.datetime.now)
    modified_at = peewee.DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = db