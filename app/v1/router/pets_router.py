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

from app.v1.service.auth_service import get_user, get_location, get_specie


router = APIRouter(prefix="/api/v1")

@router.post(
    "/user/Register-Pet",
    tags=["users"],
    status_code=status.HTTP_201_CREATED,
    response_model=pets_schema.Pets,
    dependencies=[Depends(get_db)]
)
def create_pet(pet: pets_schema.PetsBase = Body(...),  user_email: User = Depends(get_user), location_name: Location = Depends(get_location), species_name: Species = Depends(get_specie)):
    return pets_service.create_pet(pet,user_email, location_name, species_name)

@router.get(
    "/user/get-pet",
    tags=["users"],
    status_code = status.HTTP_200_OK,
    response_model=pets_schema.Pets,
    dependencies=[Depends(get_db)]
)
def get_pet(
    id_pet: int,
    email: str
):
    return pets_service.get_pet(id_pet= id_pet, email = email)