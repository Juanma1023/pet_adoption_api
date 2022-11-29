import datetime

from fastapi import HTTPException, status

from app.v1.model.request_model import Request as RequestModel
from app.v1.model.user_model import User as UserModel
from app.v1.schema import pets_schema
from app.v1.schema import user_schema
from app.v1.schema import request_schema




def create_request(request: request_schema.RequestBase, user: user_schema.User,pet: pets_schema.Pets):
    if not user:
        raise  HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Usuario no encontrado"
    )

    if not pet:
        raise  HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Mascota no encontrada"
    )
    
    db_request = RequestModel(
        description = request.description,
        user_id = user.id,
        pet_id = pet.id,
        
    )

    db_request.save()

    return request_schema.Request(
        id= db_request.id,
        description= db_request.description,
        status_request = db_request.status_request,
        created_at= db_request.created_at,
        modified_at= db_request.modified_at)

def get_request(id_req: int):
    request = RequestModel.filter((RequestModel.id == id_req)).first()
    user = request.user

    if not request:
        raise HTTPException(
            status_code= status.HTTP_404_NOT_FOUND,
            detail= "Solicitud no encontrada"
        )
    
    return request_schema.Request(
        description= request.description,
        id= request.id,
        status_request= request.status_request,
        user = request.user_id,
        pet = request.pet_id
        )

def update_request_user(id: int, description: str, modified_at = datetime.datetime.now()):
    request = RequestModel.filter(RequestModel.id == id).first()
    if not request :
        raise HTTPException(
            status_code= status.HTTP_404_NOT_FOUND,
            detail= "Mascosta no encontrada"
        )
    request.id = id
    request.description = description
    request.modified_at = modified_at
    

    request.save()

    return request_schema.Request(
        id = request.id,
        description = request.description,
        status_request = request.status_request
    )

def update_request_admin(id: int, status_request: bool, modified_at = datetime.datetime.now()):
    request = RequestModel.filter(RequestModel.id == id).first()
    if not request :
        raise HTTPException(
            status_code= status.HTTP_404_NOT_FOUND,
            detail= "Mascosta no encontrada"
        )
    request.status_request = status_request
    request.modified_at = modified_at
    

    request.save()

    return request_schema.Request(
        id = request.id,
        description = request.description,
        status_request = request.status_request
    )

def get_list_request(id_user: int):
    request = RequestModel.filter((RequestModel.user == id_user)).order_by(RequestModel.created_at.desc())
    
    if request is None:
        return "Usuario no encontrado o no posee solicitudes"

    list_req = []
    for req in request:
        list_req.append(request_schema.Request(
            id = req.id,
            status_request= req.status_request,
            description= req.description,
            created_at= req.created_at,
            modified_at= req.modified_at
        )
    )
    return list_req

def get_list_request_admin():
    list_req = []
    for i in range(0, 100):
        request = RequestModel.filter((RequestModel.id ==i)).first()
        if request is None:
            i += 1
        else:
            list_req.append(request_schema.Request(
                id = request.id,
                status_request= request.status_request,
                description= request.description,
                created_at= request.created_at,
                modified_at= request.modified_at
            )
        )
    return list_req

def delete_request(id_req: int):
    request = RequestModel.filter((RequestModel.id == id_req)).first()

    if request is None:
        raise HTTPException(
            status_code= status.HTTP_400_BAD_REQUEST,
            detail= "Solicitud no encontrada"
        )

    request.delete_instance()
