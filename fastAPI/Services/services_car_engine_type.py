
from fastAPI.Models.models_car_engine_type import Car_EngineType
from sqlalchemy.orm import Session
from fastAPI.DTO.dto_car_engine_type import Car_EngineTypeDto


#для модели Car_EngineType

def create_car_engine_type(car_engine_type_dto: Car_EngineTypeDto, db_session: Session):
    car_engine_type = Car_EngineType(
        car_engine_type=car_engine_type_dto.car_engine_type
    )

    try:
        db_session.add(car_engine_type)
        db_session.commit()
        db_session.refresh(car_engine_type)
    except Exception as e:
        print(car_engine_type)
    return car_engine_type

def get_car_engine_type(id: int, db_session: Session):
    return db_session.query(Car_EngineType).filter(Car_EngineType.id == id).first()

def get_all_car_engine_type(db_session: Session):
    return db_session.query(Car_EngineType).all()

def update_car_engine_type(id: int, car_engine_type_dto: Car_EngineTypeDto, db_session: Session):

    car_engine_type = db_session.query(Car_EngineType).filter(Car_EngineType.id == id).first()
    car_engine_type.car_engine_type = car_engine_type_dto.car_engine_type

    try:
        db_session.add(car_engine_type)
        db_session.commit()
        db_session.refresh(car_engine_type)
    except Exception as e:
        print(car_engine_type)
    return car_engine_type

def delete_car_engine_type(id: int, db_session: Session):
    db_session.query(Car_EngineType).filter(Car_EngineType.id == id).delete()
    db_session.commit()
    return

