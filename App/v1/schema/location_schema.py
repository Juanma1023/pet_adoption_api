from pydantic import BaseModel
from pydantic import Field
from pydantic import EmailStr


class LocationBase(BaseModel):
    name_city_location: str = Field(...,example="Medellin")
    latitude_location: float = Field(...,example = "6.3604762908286325")
    longitude_location: float = Field(...,example="-75.71585590821519")


class Location(LocationBase):
    id: int = Field(...,example="5")
