from fastapi import APIRouter
from fastapi import status
from fastapi import Body

from app.v1.schema import species_schema
from app.v1.service import species_service

from app.v1.utils.db import get_db


router = APIRouter(prefix="/api/v1")

@router.post(
    "/admin/species",
    tags=["admin"],
    status_code=status.HTTP_201_CREATED,
    response_model=species_schema.Species,
    summary="Create a new specie"
)
def create_specie(specie: species_schema.SpeciesBase = Body(...)):
    return species_service.create_specie(specie)