from fastapi import APIRouter
from fastapi import status
from fastapi import Body
from fastapi import Depends

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

@router.get(
    "/admin/species/{id}",
    tags=["admin"],
    status_code=status.HTTP_200_OK,
    response_model=species_schema.Species,
    dependencies = [Depends(get_db)]
)
def get_species(id_specie: int):
    return species_service.get_specie(id_specie)

@router.get(
    "/admin/get-list_species",
    tags=["admin"], 
    status_code=status.HTTP_200_OK
)
def get_species_list():
    return species_service.get_list_species()


@router.delete("/admin/delete-specie/{id}", tags=["admin"], status_code=status.HTTP_200_OK)
def delete_specie(id: int):
    species_service.delete_specie(id)
    return {
        'Msg': ' Especie eliminada satisfactoramente'
    }