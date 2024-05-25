
from fastAPI.Models.models_car_engine import Car_Engine
from sqlalchemy.orm import Session
from fastAPI.DTO.dto_car_engine import Car_EngineDto


#для модели Car_Engine

def create_car_engine(car_engine_dto: Car_EngineDto, db_session: Session):
    car_engine = Car_Engine(
        car_engine=car_engine_dto.car_engine
    )

    try:
        db_session.add(car_engine)
        db_session.commit()
        db_session.refresh(car_engine)
    except Exception as e:
        print(car_engine)
    return car_engine

def get_car_engine(id: int, db_session: Session):
    return db_session.query(Car_Engine).filter(Car_Engine.id == id).first()

def get_all_car_engine(db_session: Session):
    return db_session.query(Car_Engine).all()

def update_car_engine(id: int, car_engine_dto: Car_EngineDto, db_session: Session):

    car_engine = db_session.query(Car_Engine).filter(Car_Engine.id == id).first()
    car_engine.car_engine = car_engine_dto.car_engine

    try:
        db_session.add(car_engine)
        db_session.commit()
        db_session.refresh(car_engine)
    except Exception as e:
        print(car_engine)
    return car_engine

def delete_car_engine(id: int, db_session: Session):
    db_session.query(Car_Engine).filter(Car_Engine.id == id).delete()
    db_session.commit()
    return
