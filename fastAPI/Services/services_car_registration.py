
from fastAPI.Models.models_car_registration import Car_Registration
from sqlalchemy.orm import Session
from fastAPI.DTO.dto_car_registration import Car_RegistrationDto


#для модели Car_Registration

def create_car_registration(car_registration_dto: Car_RegistrationDto, db_session: Session):
    car_registration = Car_Registration(
        username=car_registration_dto.username,
        email=car_registration_dto.email,
        password=car_registration_dto.password
    )

    try:
        db_session.add(car_registration)
        db_session.commit()
        db_session.refresh(car_registration)
    except Exception as e:
        print(car_registration)
    return car_registration

def get_car_registration(id: int, db_session: Session):
    return db_session.query(Car_Registration).filter(Car_Registration.id == id).first()

def get_all_car_registration(db_session: Session):
    return db_session.query(Car_Registration).all()

def update_car_registration(id: int, car_registration_dto: Car_RegistrationDto, db_session: Session):

    car_registration = db_session.query(Car_Registration).filter(Car_Registration.id == id).first()
    car_registration.car_engine_type = car_registration_dto.car_registration

    try:
        db_session.add(car_registration)
        db_session.commit()
        db_session.refresh(car_registration)
    except Exception as e:
        print(car_registration)
    return car_registration

def delete_car_registration(id: int, db_session: Session):
    db_session.query(Car_Registration).filter(Car_Registration.id == id).delete()
    db_session.commit()
    return

