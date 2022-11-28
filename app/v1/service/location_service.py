from fastapi import HTTPException, status


from app.v1.model.location_model import Location as LocationModel
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