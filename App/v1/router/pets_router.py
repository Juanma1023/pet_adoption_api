from fastapi import APIRouter
from fastapi import Depends
from fastapi import status
from fastapi import Body

from app.v1.schema import pets_schema
from app.v1.service import pets_service

from app.v1.utils.db import get_db
from app.v1.schema.user_schema import User
from app.v1.schema.location_schema import Location
from app.v1.schema.species_schema import Species

from app.v1.service.auth_service import get_user, get_location, get_specie, get_email_users

router = APIRouter(prefix="/api/v1")

@router.post(
        "/user/Register-Pet",
        tags=["users"],
        status_code=status.HTTP_201_CREATED,
        response_model=pets_schema.Pets,
        dependencies=[Depends(get_db)]
    )
def create_pet(
        pet: pets_schema.PetsBase = Body(...),
        user_email: User = Depends(get_user),
        location_name: Location = Depends(get_location),
        species_name: Species = Depends(get_specie)
        ):
    return pets_service.create_pet(pet,user_email, location_name, species_name)

@router.get(
    "/users/get_pet/{id}",
    tags=["users"],
    status_code=status.HTTP_200_OK,
    response_model=pets_schema.Pets,
    dependencies=[Depends(get_db)]
)
def get_pet_at(
    id_pet: int
):
    return pets_service.get_pet(id_pet)

@router.put(
    "/user/pet/{id}/modificaciones",
    tags=["users"],
    status_code=status.HTTP_200_OK,
    response_model=pets_schema.Pets,
    dependencies=[Depends(get_db)]
)
def modified_pet(id: int, name: str, age: str, gender: str, size: str, description: str, sterilized: str):
    if sterilized.lower() == "si":
        sterilized = True
    elif sterilized.lower() == "no":
        sterilized = False
    else: 
        return {
            "msg": "ingrese la opcion si o no"
        }
    return pets_service.update_pet(id, name, age, gender, size, description, sterilized)


@router.get("/user/{id}/list_pets",
tags=["users"], status_code=status.HTTP_200_OK, dependencies= [Depends(get_db)])
def get_list_pets_user(id_user: int):
    return pets_service.get_list_pets(id_user)

@router.delete("/user/delete-pet/{id}", tags=["users"], status_code=status.HTTP_200_OK)
def delete_pet(id: int):
    pets_service.delete_pet(id)
    return {
        'Msg': ' Mascota eliminada satisfactoramente'
    }

