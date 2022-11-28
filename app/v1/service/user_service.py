from fastapi import HTTPException, status
from pydantic import EmailStr


from app.v1.model.user_model import User as UserModel
from app.v1.model.pets_model import Pets as PetsModel
from app.v1.model.request_model import Request as RequestModel
from app.v1.schema import user_schema
from app.v1.schema import pets_schema


def create_user(user: user_schema.UserBase):
    get_user = UserModel.filter(UserModel.email == user.email).first()
    if get_user:
        if get_user.email == user.email:
            msg = "Correo ya existente"
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=msg
        )

    db_user = UserModel(
        name = user.name,
        last_name = user.last_name,
        phone = user.phone,
        email = user.email,
        address= user.address
    )

    db_user.save()

    return user_schema.User(
        id = db_user.id,
        name = db_user.name,
        last_name = db_user.last_name,
        phone = db_user.phone,
        email = db_user.email,
        address= db_user.address
    )

def get_user(email: str):
    user = UserModel.filter((UserModel.email== email)).first()

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Usuario no encontrado"
        )

    return user_schema.User(
        id = user.id,
        name = user.name,
        last_name = user.last_name,
        phone = user.phone,
        email = user.email,
        address= user.address
    )

def delete_user(id_user: int):
    user = UserModel.filter((UserModel.id == id_user)).first()
    pets = PetsModel.filter((PetsModel.user == id_user)).first()
    request = RequestModel.filter((RequestModel.user == id_user)).first()

    if pets or request is not None:
        raise HTTPException(
            status_code= status.HTTP_400_BAD_REQUEST,
            detail= "Usuario no puede ser eliminado, posee mascotas"
        )

    if not user:
        raise HTTPException(
            status_code= status.HTTP_404_NOT_FOUND,
            detail= "Usuario no encontrado"
        )

    user.delete_instance()