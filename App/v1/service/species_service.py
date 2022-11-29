from fastapi import HTTPException, status


from app.v1.model.species_pet_model import Species as SpeciesModel
from app.v1.model.pets_model import Pets as PetsModel

from app.v1.schema import species_schema


def create_specie(specie: species_schema.SpeciesBase):
    get_specie = SpeciesModel.filter(SpeciesModel.name_species == specie.name_species).first()
    if get_specie:
        if get_specie.name_species == specie.name_species:
            msg = "Especie ya existente"
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=msg
        )

    db_specie = SpeciesModel(
        name_species=specie.name_species
    )

    db_specie.save()

    return species_schema.Species(
        id = db_specie.id,
        name_species= db_specie.name_species,
        enabled= db_specie.enabled
    )

def get_specie(id: int):
    specie = SpeciesModel.filter(SpeciesModel.id == id).first()
    if not specie:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Especie no encontrada"
        )

    return species_schema.Species(
        id = specie.id,
        name_species= specie.name_species,
        enabled= specie.enabled 
    )

def get_list_species():
    list_species = []
    for i in range(0, 100):
        specie = SpeciesModel.filter(SpeciesModel.id == i).first()
        if specie is None:
            i += 1
        else:
            list_species.append(species_schema.Species(
                id= specie.id,
                name_species= specie.name_species,
                enabled= specie.enabled
            ))

    return list_species


def delete_specie(specie_id: int):
    specie = SpeciesModel.filter((SpeciesModel.id == specie_id)).first()
    pets = PetsModel.filter((PetsModel.species == specie_id)).first()

    if pets is not None:
        raise HTTPException(
            status_code= status.HTTP_400_BAD_REQUEST,
            detail= "Esta especie no puede ser eliminada, se encuentra en uso"
        )

    if specie is None:
        raise HTTPException(
            status_code= status.HTTP_400_BAD_REQUEST,
            detail= "Especie no encontrada"
        )

    specie.delete_instance()