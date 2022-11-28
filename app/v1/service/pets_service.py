from fastapi import HTTPException, status

from app.v1.model.pets_model import Pets as PetsModel
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

def get_pet(id_pet , user: user_schema.User):
    pet = PetsModel.filter((PetsModel.id == id_pet) & (PetsModel.user == user.id)).first()
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

def get_pets(user: user_schema.User):
    pets = PetsModel.filter(PetsModel.user == user.id)
    
    list_pets = []
    for pet in pets:
        list_pets.append(pets_schema.Pets(
                            id = pet.id,
                            name = pet.name,
                            age = pet.age,
                            size = pet.size,
                            created_at= pet.created_at))
    return list_pets
    