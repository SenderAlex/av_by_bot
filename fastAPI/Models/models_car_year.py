
from sqlalchemy import Column, Integer, String
from fastAPI.database import Base


class Car_Year(Base):
    __tablename__ = 'tele_bot_app_car_year'
    id = Column(Integer, primary_key=True)
    car_year = Column(String)
