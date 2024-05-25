
from sqlalchemy import Column, Integer, String
from fastAPI.database import Base


class Car_EngineType(Base):
    __tablename__ = 'tele_bot_app_car_enginetype'
    id = Column(Integer, primary_key=True)
    car_engine_type = Column(String)
