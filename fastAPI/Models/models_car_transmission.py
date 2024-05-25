
from sqlalchemy import Column, Integer, String
from fastAPI.database import Base


class Car_Transmission(Base):
    __tablename__ = 'tele_bot_app_car_transmission'
    id = Column(Integer, primary_key=True)
    car_transmission = Column(String)
