from fastapi import HTTPException, status


from app.v1.model.species_pet_model import Species as SpeciesModel
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