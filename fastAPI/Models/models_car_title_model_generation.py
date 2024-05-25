
from sqlalchemy import Column, Integer, String, ForeignKey
from fastAPI.database import Base


class Car_Title(Base):
    __tablename__ = 'tele_bot_app_car_title'
    id = Column(Integer, primary_key=True)
    car_title = Column(String)

class Car_Model(Base):
    __tablename__ = 'tele_bot_app_car_model'
    id = Column(Integer, primary_key=True)
    car_model = Column(String)
    car_title_id_id = Column(Integer, ForeignKey('tele_bot_app_car_title.id'))

class Car_Generation(Base):
    __tablename__ = 'tele_bot_app_car_generation'
    id = Column(Integer, primary_key=True)
    car_generation = Column(String)
    car_model_id_id = Column(Integer, ForeignKey('tele_bot_app_car_model.id'))
