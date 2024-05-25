
from fastAPI.Models.models_car_year import Car_Year
from sqlalchemy.orm import Session
from fastAPI.DTO.dto_car_year import Car_YearDto


#для модели Car_Year

def create_car_year(car_year_dto: Car_YearDto, db_session: Session):
    car_year = Car_Year(
        car_year=car_year_dto.car_year
    )

    try:
        db_session.add(car_year)
        db_session.commit()
        db_session.refresh(car_year)
    except Exception as e:
        print(car_year)
    return car_year

def get_car_year(id: int, db_session: Session):
    return db_session.query(Car_Year).filter(Car_Year.id == id).first()

def get_all_car_year(db_session: Session):
    return db_session.query(Car_Year).all()

def update_car_year(id: int, car_year_dto: Car_YearDto, db_session: Session):

    car_year = db_session.query(Car_Year).filter(Car_Year.id == id).first()
    car_year.car_year = car_year_dto.car_year

    try:
        db_session.add(car_year)
        db_session.commit()
        db_session.refresh(car_year)
    except Exception as e:
        print(car_year)
    return car_year

def delete_car_year(id: int, db_session: Session):
    db_session.query(Car_Year).filter(Car_Year.id == id).delete()
    db_session.commit()
    return
