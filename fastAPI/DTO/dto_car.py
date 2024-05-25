
from pydantic import BaseModel


class CarDto(BaseModel):

    car_title: str
    car_model: str
    car_generation: str
    car_vin: str
    main_car_image: str
    car_images: str
    year: int
    transmission: str
    engine: str
    fuel: str
    car_body: str
    car_drive: str
    car_color: str
    horse_power: str
    consumption: str
    mileage: int
    price_byn: int
    price_usd: int
    city: str
    description: str
    car_options: str
    http_link: str
