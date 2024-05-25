
from pydantic import BaseModel


class LoginRequest(BaseModel):

    email: str
    password: str

class LoginResponse(BaseModel):
    message: str

    class Config:
        arbitrary_types_allowed = True
        response_model_exclude_unset = True