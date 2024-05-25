
from fastAPI.Models.models_car_transmission import Car_Transmission
from sqlalchemy.orm import Session
from fastAPI.DTO.dto_car_transmission import Car_TransmissionDto


#для модели Car_Transmission

def create_car_transmission(car_transmission_dto: Car_TransmissionDto, db_session: Session):
    car_transmission = Car_Transmission(
        car_transmission=car_transmission_dto.car_transmission
    )

    try:
        db_session.add(car_transmission)
        db_session.commit()
        db_session.refresh(car_transmission)
    except Exception as e:
        print(car_transmission)
    return car_transmission

def get_car_transmission(id: int, db_session: Session):
    return db_session.query(Car_Transmission).filter(Car_Transmission.id == id).first()

def get_all_car_transmission(db_session: Session):
    return db_session.query(Car_Transmission).all()

def update_car_transmission(id: int, car_transmission_dto: Car_TransmissionDto, db_session: Session):

    car_transmission = db_session.query(Car_Transmission).filter(Car_Transmission.id == id).first()
    car_transmission.car_transmission = car_transmission_dto.car_transmission

    try:
        db_session.add(car_transmission)
        db_session.commit()
        db_session.refresh(car_transmission)
    except Exception as e:
        print(car_transmission)
    return car_transmission

def delete_car_transmission(id: int, db_session: Session):
    db_session.query(Car_Transmission).filter(Car_Transmission.id == id).delete()
    db_session.commit()
    return

