from fastapi import Depends, HTTPException, status
from app.v1.schema.user_schema import UserBase
from app.v1.schema.location_schema import LocationBase
from app.v1.schema.species_schema import SpeciesBase
from app.v1.schema.pets_schema import Pets


from pydantic import EmailStr



from app.v1.model.user_model import User as UserModel
from app.v1.model.pets_model import Pets as PetsModel
from app.v1.model.location_model import Location as LocationModel
from app.v1.model.species_pet_model import Species as SpeciesModel
from app.v1.utils.settings import Settings

settings = Settings()



def get_user(user_email:str):
    get_user_at = UserModel.filter(UserModel.email == user_email).first()
    print(get_user_at)
    return get_user_at

async def get_email_users(email: str):
    email_exception = HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Usuario no encontrado"
    )

    email = get_user(user_email=UserBase.Config.get('user_email'))
    print(email)
    if email is None:
        raise email_exception
    return email


def get_location(name_location: str):
    return LocationModel.filter((LocationModel.name_city_location == name_location) ).first()

async def get_name_locations(location: str):
    location_exception = HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Ubicacion no encontrada"
    )
    location = get_location(name_location=LocationBase.Config.get('name_location'))
    if location == None:
        raise location_exception
    return location


def get_specie(name_specie: str):
    return SpeciesModel.filter(SpeciesModel.name_species == name_specie).first()

async def get_species(specie_name: str):
    exception = HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Especie No encontrado"
    )
    specie_name = get_specie(name_specie=SpeciesBase.Config.get('name_specie'))
    if specie_name is None:
        raise exception
    return specie_name


def get_pet(id_pet: int):
    return PetsModel.filter((PetsModel.id == id_pet) ).first()

async def get_id_pet(id: int):
    pet_exception = HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Mascota no encontrada"
    )
    id = get_pet(id_pet=Pets.get('id'))
    if id == None:
        raise pet_exception
    return id
