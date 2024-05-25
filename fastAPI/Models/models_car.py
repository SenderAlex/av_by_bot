
from sqlalchemy import Column, Integer, String
from fastAPI.database import Base


class Car(Base):
    __tablename__ = 'tele_bot_app_car'

    id = Column(Integer, primary_key=True)
    car_title = Column(String)
    car_model = Column(String)
    car_generation = Column(String)
    car_vin = Column(String)
    main_car_image = Column(String)
    car_images = Column(String)
    year = Column(Integer)
    transmission = Column(String)
    engine = Column(String)
    fuel = Column(String)
    car_body = Column(String)
    car_drive = Column(String)
    car_color = Column(String)
    horse_power = Column(String)
    consumption = Column(String)
    mileage = Column(Integer)
    price_byn = Column(Integer)
    price_usd = Column(Integer)
    city = Column(String)
    description = Column(String)
    car_options = Column(String)
    http_link = Column(String)
