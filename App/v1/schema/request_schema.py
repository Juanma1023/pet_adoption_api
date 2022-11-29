from datetime import datetime

from pydantic import BaseModel
from pydantic import Field


class RequestBase(BaseModel):
    description: str = Field(...,example="Deseo adoptar porque me gustan los animales")

class Request(RequestBase):
    id: int = Field(...)
    status_request: bool = Field(default=False)
    created_at: datetime = Field(default= datetime.now())  
    modified_at:  datetime = Field(default= datetime.now()) 

