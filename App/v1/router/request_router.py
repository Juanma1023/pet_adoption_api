from fastapi import APIRouter
from fastapi import Depends
from fastapi import status
from fastapi import Body

from app.v1.schema import request_schema
from app.v1.service import request_service

from app.v1.utils.db import get_db
from app.v1.schema.user_schema import User
from app.v1.schema.pets_schema import Pets

from app.v1.service.auth_service import get_user, get_pet



router = APIRouter(prefix="/api/v1")

@router.post(
    "/user/Solicitudes",
    tags=["users"],
    status_code=status.HTTP_201_CREATED,
    response_model=request_schema.Request,
    dependencies=[Depends(get_db)]
)
def create_request(request: request_schema.RequestBase = Body(...),  user_email: User = Depends(get_user), pet_id: Pets = Depends(get_pet)):
    return request_service.create_request(request,user_email, pet_id)

@router.get(
    "/user/request/{id}",
    tags=["users"],
    status_code= status.HTTP_200_OK,
    response_model= request_schema.Request,
    dependencies=[Depends(get_db)]
)
def get_request(id: int):
    return request_service.get_request(id)

@router.put(
    "/user/request/{id}/modificaciones",
    tags=["users"],
    status_code=status.HTTP_200_OK,
    response_model=request_schema.Request,
    dependencies=[Depends(get_db)]
)
def modified_request(id: int, description: str):
    return request_service.update_request_user(id, description) 

@router.put(
    "/admin/request/{id}/modificaciones",
    tags=["admin"],
    status_code=status.HTTP_200_OK,
    response_model=request_schema.Request,
    dependencies=[Depends(get_db)]
)
def modified_request(id: int, status_request: str):
    if status_request.lower() == "aceptado":
        status_request = True
    elif status_request.lower() == "rechazado":
        status_request = False
    else:
        return {
            "msg": "Ingrese un valor correcto, Aceptado o Rechazado"
        }
    return request_service.update_request_admin(id,status_request)

@router.get("/user/{id}/list_request",
tags=["users"], status_code=status.HTTP_200_OK, dependencies= [Depends(get_db)])
def get_list_request_user(id_user: int):
    return request_service.get_list_request(id_user)

@router.delete("/user/request/delete/{id}", tags=["users"], status_code=status.HTTP_200_OK)
def delete_request(id: int):
    request_service.delete_request(id)
    return {
        'Msg': 'Solicitud eliminada satisfactoramente'
    }