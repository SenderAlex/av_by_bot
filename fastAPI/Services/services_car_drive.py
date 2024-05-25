
from fastAPI.Models.models_car_drive import Car_Drive
from sqlalchemy.orm import Session
from fastAPI.DTO.dto_car_drive import Car_DriveDto


#для модели Car_Drive

def create_car_drive(car_drive_dto: Car_DriveDto, db_session: Session):
    car_drive = Car_Drive(
        car_drive=car_drive_dto.car_drive
    )

    try:
        db_session.add(car_drive)
        db_session.commit()
        db_session.refresh(car_drive)
    except Exception as e:
        print(car_drive)
    return car_drive

def get_car_drive(id: int, db_session: Session):
    return db_session.query(Car_Drive).filter(Car_Drive.id == id).first()

def get_all_car_drive(db_session: Session):
    return db_session.query(Car_Drive).all()

def update_car_drive(id: int, car_drive_dto: Car_DriveDto, db_session: Session):

    car_drive = db_session.query(Car_Drive).filter(Car_Drive.id == id).first()
    car_drive.car_drive = car_drive_dto.car_drive

    try:
        db_session.add(car_drive)
        db_session.commit()
        db_session.refresh(car_drive)
    except Exception as e:
        print(car_drive)
    return car_drive

def delete_car_drive(id: int, db_session: Session):
    db_session.query(Car_Drive).filter(Car_Drive.id == id).delete()
    db_session.commit()
    return

