
from fastAPI.Models.models_car import Car
from sqlalchemy.orm import Session
from fastAPI.DTO.dto_car import CarDto


#для модели Car
def create_car(car_dto: CarDto, db_session: Session):
    car = Car(
        car_title=car_dto.car_title,
        car_model=car_dto.car_model,
        car_generation=car_dto.car_generation,
        car_vin=car_dto.car_vin,
        main_car_image=car_dto.main_car_image,
        car_images=car_dto.car_images,
        year=car_dto.year,
        transmission=car_dto.transmission,
        engine=car_dto.engine,
        fuel=car_dto.fuel,
        car_body=car_dto.car_body,
        car_drive=car_dto.car_drive,
        color=car_dto.color,
        horse_power=car_dto.horse_power,
        consumption=car_dto.consumption,
        mileage=car_dto.mileage,
        price_byn=car_dto.price_byn,
        price_usd=car_dto.price_usd,
        city=car_dto.city,
        description=car_dto.description,
        car_options=car_dto.car_options,
        http_link=car_dto.http_link
    )

    try:
        db_session.add(car)
        db_session.commit()
        db_session.refresh(car)
    except Exception as e:
        print(car)
    return car

def get_car(id: int, db_session: Session):
    return db_session.query(Car).filter(Car.id == id).first()

def get_all_car(db_session: Session):
    return db_session.query(Car).all()

def update_car(id: int, car_dto: CarDto, db_session: Session):
    car = db_session.query(Car).filter(Car.id == id).first()
    car.car_title = car_dto.car_title,
    car.car_model = car_dto.car_model,
    car.car_generation = car_dto.car_generation,
    car.car_vin = car_dto.car_vin,
    car.main_car_image = car_dto.main_car_image,
    car.car_images = car_dto.car_images,
    car.year = car_dto.year,
    car.transmission = car_dto.transmission,
    car.engine = car_dto.engine,
    car.fuel = car_dto.fuel,
    car.car_body = car_dto.car_body,
    car.car_drive = car_dto.car_drive,
    car.color = car_dto.color,
    car.horse_power = car_dto.horse_power,
    car.consumption = car_dto.consumption,
    car.mileage = car_dto.mileage,
    car.price_byn = car_dto.price_byn,
    car.price_usd = car_dto.price_usd,
    car.city = car_dto.city,
    car.description = car_dto.description,
    car.car_options = car_dto.car_options,
    car.http_link = car_dto.http_link

    try:
        db_session.add(car)
        db_session.commit()
        db_session.refresh(car)
    except Exception as e:
        print(car)
    return car

def delete_car(id: int, db_session: Session):
    db_session.query(Car).filter(Car.id == id).delete()
    db_session.commit()
    return

