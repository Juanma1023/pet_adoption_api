import datetime
import peewee

from app.v1.utils.db import db

from app.v1.model.user_model import User
from app.v1.model.pets_model import Pets

class Request(peewee.Model):
    description = peewee.CharField()
    created_at = peewee.DateTimeField(default=datetime.datetime.now)
    modified_at = peewee.DateTimeField(default=datetime.datetime.now)
    status_request = peewee.BooleanField(default=False)
    user = peewee.ForeignKeyField(User, backref="Users")
    pet = peewee.ForeignKeyField(Pets, backref="Pets")
    

    class Meta:
        database = db 