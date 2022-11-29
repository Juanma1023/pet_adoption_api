from fastapi import HTTPException, status


from app.v1.model.location_model import Location as LocationModel
from app.v1.model.pets_model import Pets as PetsModel
from app.v1.schema import location_schema


def create_location(location: location_schema.LocationBase):
    get_location = LocationModel.filter(LocationModel.name_city_location == location.name_city_location).first()
    if get_location:
        if get_location.name_city_location == location.name_city_location:
            msg = "Ciudad ya existente"
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=msg
        )

    db_location = LocationModel(
        name_city_location = location.name_city_location,
        longitude_location = location.longitude_location,
        latitude_location = location.latitude_location
    )

    db_location.save()

    return location_schema.Location(
        id = db_location.id,
        name_city_location = db_location.name_city_location,
        longitude_location = db_location.longitude_location,
        latitude_location = db_location.latitude_location
    )

def get_location(id: int):
    location = LocationModel.filter(LocationModel.id == id).first()
    if not location:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Ubicacion no encontrada"
        )

    return location_schema.Location(
        id = location.id,
        name_city_location= location.name_city_location,
        latitude_location= location.latitude_location,
        longitude_location= location.longitude_location
    )

def get_list_locations():
    list_location = []
    for i in range(0, 100):
        location = LocationModel.filter((LocationModel.id == i)).first()
        if location is None:
            i += 1
        else:
            list_location.append(location_schema.Location(
                id = location.id,
                name_city_location= location.name_city_location,
                latitude_location= location.latitude_location,
                longitude_location= location.longitude_location
    ))
    return list_location


def delete_location(location_id: int):
    location = LocationModel.filter((LocationModel.id == location_id)).first()
    pets = PetsModel.filter((PetsModel.location == location_id)).first()

    if pets is not None:
        raise HTTPException(
            status_code= status.HTTP_400_BAD_REQUEST,
            detail= "Ubicacion no puede ser eliminada, se encuentra en uso"
        )

    if location is None:
        raise HTTPException(
            status_code= status.HTTP_400_BAD_REQUEST,
            detail= "Ubicacion no encontrada"
        )

    location.delete_instance()



