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