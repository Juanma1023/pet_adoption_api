from datetime import datetime

from pydantic import BaseModel
from pydantic import Field
from pydantic import EmailStr


class UserBase(BaseModel):
    name: str = Field(...,example="Jose Daniel")
    last_name: str = Field(...,example="Foronda")
    phone: str = Field(...,example="3123123101")
    email: EmailStr = Field(...,example="jdaniel.foranda@udea.edu.co")
    address: str = Field(...,example="Medellin, Cr. 12#20-19")

class User(UserBase):
    id: int = Field(...)
    created_at: datetime = Field(default= datetime.now())  
    modified_at:  datetime = Field(default= datetime.now()) 