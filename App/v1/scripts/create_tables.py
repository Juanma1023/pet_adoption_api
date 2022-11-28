from app.v1.model.user_model import User
from app.v1.model.pets_model import Pets
from app.v1.model.location_model import Location
from app.v1.model.species_pet_model import Species
from app.v1.model.request_model import Request


from app.v1.utils.db import db

def create_tables():
    with db:
        db.create_tables([User, Pets, Species, Request, Location])
