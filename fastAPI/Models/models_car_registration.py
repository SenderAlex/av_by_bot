
from sqlalchemy import Column, Integer, String
from fastAPI.database import Base


class Car_Registration(Base):
    __tablename__ = 'tele_bot_app_registration'
    id = Column(Integer, primary_key=True)
    username = Column(String)
    email = Column(String)
    password = Column(String)

    __table_args__ = {"extend_existing": True}