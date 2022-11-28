from fastapi import APIRouter
from fastapi import status
from fastapi import Body

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