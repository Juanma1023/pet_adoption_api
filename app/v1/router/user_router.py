from fastapi import APIRouter
from fastapi import Depends
from pathlib import Path
from fastapi import status
from fastapi import Body
from typing import List

from app.v1.schema import user_schema
from app.v1.schema import pets_schema
from app.v1.service import pets_service
from app.v1.service import user_service
from app.v1.schema.user_schema import User
from app.v1.service.auth_service import get_email_users

from app.v1.utils.db import get_db


router = APIRouter(prefix="/api/v1")

@router.post(
    "/user/",
    tags=["users"],
    status_code=status.HTTP_201_CREATED,
    response_model=user_schema.User,
    dependencies= [Depends(get_db)],
    summary="Usuario creado correctamente"
)
def create_user(
    user: user_schema.UserBase = Body(...)
):
    return user_service.create_user(user)

@router.get(
    "/user/{id}",
    tags=["users"],
    status_code=status.HTTP_200_OK,
    response_model=user_schema.User,
    dependencies= [Depends(get_db)]
)
def get_one_user(
    email: str
):
    return user_service.get_user(email)

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

@router.delete("/user/delete/{id}", tags=["users"], status_code=status.HTTP_200_OK)
def delete_user(id: int):
    user_service.delete_user(id)
    return {
        'Msg': 'Usuario eliminado satisfactoramente'
    }


