
from sqlalchemy import Column, Integer, String
from fastAPI.database import Base


class Car_Drive(Base):
    __tablename__ = 'tele_bot_app_car_drive'
    id = Column(Integer, primary_key=True)
    car_drive = Column(String)