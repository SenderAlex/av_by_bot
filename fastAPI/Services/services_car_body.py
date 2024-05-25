
from fastAPI.Models.models_car_body import Car_Body
from sqlalchemy.orm import Session
from fastAPI.DTO.dto_car_body import Car_BodyDto


#для модели Car_Body

def create_car_body(car_body_dto: Car_BodyDto, db_session: Session):
    car_body = Car_Body(
        car_body=car_body_dto.car_body
    )

    try:
        db_session.add(car_body)
        db_session.commit()
        db_session.refresh(car_body)
    except Exception as e:
        print(car_body)
    return car_body

def get_car_body(id: int, db_session: Session):
    return db_session.query(Car_Body).filter(Car_Body.id == id).first()

def get_all_car_body(db_session: Session):
    return db_session.query(Car_Body).all()

def update_car_body(id: int, car_body_dto: Car_BodyDto, db_session: Session):

    car_body = db_session.query(Car_Body).filter(Car_Body.id == id).first()
    car_body.car_body = car_body_dto.car_body

    try:
        db_session.add(car_body)
        db_session.commit()
        db_session.refresh(car_body)
    except Exception as e:
        print(car_body)
    return car_body

def delete_car_body(id: int, db_session: Session):
    db_session.query(Car_Body).filter(Car_Body.id == id).delete()
    db_session.commit()
    return

