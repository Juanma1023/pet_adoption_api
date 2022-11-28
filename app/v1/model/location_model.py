import peewee

from app.v1.utils.db import db 


class Location(peewee.Model):
    name_city_location = peewee.CharField()
    latitude_location = peewee.FloatField()
    longitude_location = peewee.FloatField()

    class Meta:
        database = db 