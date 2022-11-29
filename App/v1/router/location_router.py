from fastapi import APIRouter
from fastapi import status
from fastapi import Body
from fastapi import Depends

from app.v1.schema import location_schema
from app.v1.service import location_service

from app.v1.utils.db import get_db


router = APIRouter(prefix="/api/v1")

@router.post(
    "/admin/location",
    tags=["admin"],
    status_code=status.HTTP_201_CREATED,
    response_model=location_schema.Location,
    summary="Create a new location"
)
def create_location(location: location_schema.LocationBase = Body(...)):
    return location_service.create_location(location)

@router.get(
    "/admin/location/{id}",
    tags=["admin"],
    status_code= status.HTTP_200_OK,
    response_model = location_schema.Location,
    dependencies= [Depends(get_db)]
    )
def get_location(id: int):
    return location_service.get_location(id)

@router.get(
    "/admin/get-list_location",
    tags=["admin"], 
    status_code=status.HTTP_200_OK
)
def get_locations():
    return location_service.get_list_locations()

@router.delete("/admin/delete-location/{id}", tags=["admin"], status_code=status.HTTP_200_OK)
def delete_location(id: int):
    location_service.delete_location(id)
    return {
        'Msg': ' Ubicacion eliminada satisfactoramente'
    }


