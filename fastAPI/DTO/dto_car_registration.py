
from pydantic import BaseModel


class Car_RegistrationDto(BaseModel):

    username: str
    email: str
    password: str
