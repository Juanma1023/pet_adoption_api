import datetime
import peewee

from app.v1.utils.db import db
from .user_model import User
from .location_model import Location
from .species_pet_model import Species


class Pets(peewee.Model):
    name = peewee.CharField()
    age = peewee.CharField()
    gender = peewee.CharField()
    size = peewee.CharField()
    sterilized = peewee.BooleanField(default=False)
    description = peewee.CharField()
    enabled = peewee.BooleanField(default=True)
    created_at = peewee.DateTimeField(default=datetime.datetime.now)
    modified_at = peewee.DateTimeField(default=datetime.datetime.now)
    species = peewee.ForeignKeyField(Species,backref='species')
    user = peewee.ForeignKeyField(User,backref='users')
    location = peewee.ForeignKeyField(Location, backref='locations')

    class Meta:
        database = db
