from datetime import datetime

from pydantic import BaseModel
from pydantic import Field


class PetsBase(BaseModel):
    name: str = Field(...,example="Canela")
    age: str = Field(...,example="2 años")
    gender: str = Field(...,example="Hembra")
    size: str = Field(...,example="Pequeña")
    description: str = Field(...,example="Jueguetona, amistosa y cariñosa")

class Pets(PetsBase):
    id: int = Field(...)
    sterilized: bool = Field(default=False)
    enabled: bool= Field(default=True)
    created_at: datetime = Field(default= datetime.now())  
    modified_at:  datetime = Field(default= datetime.now()) 