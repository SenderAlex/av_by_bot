
from sqlalchemy import Column, Integer, String
from fastAPI.database import Base


class Car_Engine(Base):
    __tablename__ = 'tele_bot_app_car_engine'
    id = Column(Integer, primary_key=True)
    car_engine = Column(String)
