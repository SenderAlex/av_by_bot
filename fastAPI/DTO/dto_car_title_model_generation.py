
from pydantic import BaseModel


class Car_TitleDto(BaseModel):

    car_title: str


class Car_ModelDto(BaseModel):

    car_model: str
    car_title_id_id: int


class Car_GenerationDto(BaseModel):

    car_generation: str
    car_model_id_id: int