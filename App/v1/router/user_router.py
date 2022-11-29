from fastapi import APIRouter
from fastapi import Depends
from fastapi import status
from fastapi import Body

from app.v1.schema import user_schema
from app.v1.service import user_service


from app.v1.utils.db import get_db


router = APIRouter(prefix="/api/v1")

@router.post(
        "/user/",
        tags=["users"],
        status_code=status.HTTP_201_CREATED,
        response_model=user_schema.User,
        dependencies= [Depends(get_db)]
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

@router.put(
    "/user/{id}/modificaciones",
    tags=["users"],
    status_code=status.HTTP_200_OK,
    response_model=user_schema.User,
    dependencies=[Depends(get_db)]
)
def modified_user(email: str, name: str, last_name: str, phone: int, address: str):
    return user_service.update_user(email, name, last_name, phone, address)


@router.get("/admin/list_users",
tags=["admin"], status_code=status.HTTP_200_OK, dependencies= [Depends(get_db)])
def get_list_users_admin():
    return user_service.get_list_users_admin()

@router.delete("/user/delete/{id}", tags=["users"], status_code=status.HTTP_200_OK)
def delete_user(id: int):
    user_service.delete_user(id)
    return {
        'Msg': 'Usuario eliminado satisfactoramente'
    }


