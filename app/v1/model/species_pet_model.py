import peewee

from app.v1.utils.db import db 


class Species(peewee.Model):
    name_species = peewee.CharField()
    enabled = peewee.BooleanField(default=True)

    class Meta:
        database = db 