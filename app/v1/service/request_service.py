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

    print(type(db_request.id))

    return request_schema.Request(
        id= db_request.id,
        description= db_request.description,
        status_request = db_request.status_request,
        created_at= db_request.created_at,
        modified_at= db_request.modified_at)