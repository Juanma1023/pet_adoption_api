import datetime

from fastapi import HTTPException, status

from app.v1.model.pets_model import Pets as PetsModel
from app.v1.model.user_model import User as UserModel


from app.v1.schema import pets_schema
from app.v1.schema import user_schema
from app.v1.schema import location_schema
from app.v1.schema import species_schema


def create_pet(pet: pets_schema.PetsBase, user: user_schema.User, location: location_schema.Location, species: species_schema.Species):
    if not user:
        raise  HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Usuario no encontrado")
    if not location:
        raise  HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Ubicacion no encontrada")
    if not species:
        raise  HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Especie no encontrada")
    
    db_pet = PetsModel(
        name = pet.name,
        age= pet.age,
        gender = pet.gender,
        size = pet.size,
        description = pet.description,
        user = user.id,
        location = location.id,
        species = species.id
    )

    db_pet.save()

    print(type(db_pet.id))

    return pets_schema.Pets(
        id= db_pet.id,
        name = db_pet.name,
        age = db_pet.age,
        gender = db_pet.gender,
        size = db_pet.size,
        sterilized = db_pet.sterilized,
        description = db_pet.description,
        enabled = db_pet.enabled,
        created_at= db_pet.created_at,
        modified_at= db_pet.modified_at

    )

def get_pet(id_pet: int):
    pet = PetsModel.filter((PetsModel.id == id_pet)).first()
    if not pet:
        raise HTTPException(
            status_code= status.HTTP_404_NOT_FOUND,
            detail= "Mascota no encontrada"
        )
    
    return pets_schema.Pets(
        id= pet.id,
        name= pet.name,
        age= pet.age,
        gender= pet.gender,
        size= pet.size,
        description= pet.description,
        sterilized= pet.sterilized,
        created_at= pet.created_at
    )

def update_pet(id: int, name: str, age: str, gender: str, size: str, description: str, sterilized: bool, modified_at = datetime.datetime.now()):
    pet = PetsModel.filter(PetsModel.id == id).first()
    if not pet :
        raise HTTPException(
            status_code= status.HTTP_404_NOT_FOUND,
            detail= "Mascosta no encontrada"
        )
    pet.id = id
    pet.name = name
    pet.age = age
    pet.gender = gender
    pet.size = size
    pet.description = description
    pet.sterilized = sterilized
    pet.modified_at = modified_at
    

    pet.save()

    return pets_schema.Pets(
        id = pet.id,
        name = pet.name,
        gender = pet.gender,
        age = pet.age,
        size= pet.size,
        description = pet.description,
        sterilized= pet.sterilized,
        modified_at= pet.modified_at
    )

def get_list_pets(id_user: int):
    pets = PetsModel.filter((PetsModel.user == id_user)).order_by(PetsModel.created_at.desc())
    
    if pets is None:
        return "Usuario no encontrado o no posee mascotas"

    list_pets = []
    for pet in pets:
        list_pets.append(pets_schema.Pets(
            id = pet.id,
            name = pet.name,
            age= pet.age,
            gender= pet.gender,
            size= pet.size,
            description= pet.description,
            sterilized= pet.sterilized,
            created_at= pet.created_at,
            modified_at= pet.modified_at
        ))
    return list_pets

def delete_pet(pet_id: int):
    pet = PetsModel.filter((PetsModel.id == pet_id)).first()

    if pet is None:
        raise HTTPException(
            status_code= status.HTTP_400_BAD_REQUEST,
            detail= "Mascota no encontrada"
        )

    pet.delete_instance()
    