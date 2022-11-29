from pydantic import BaseModel
from pydantic import Field

class SpeciesBase(BaseModel):
    name_species: str = Field(...,example="Perro")

class Species(SpeciesBase):
    id: int = Field(...,example="5")
    enabled: bool = Field(default=True)