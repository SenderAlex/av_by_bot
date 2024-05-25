
from fastAPI.Models.models_car_title_model_generation import Car_Title, Car_Model, Car_Generation
from sqlalchemy.orm import Session
from fastAPI.DTO.dto_car_title_model_generation import Car_TitleDto, Car_ModelDto, Car_GenerationDto


#для модели Car_Title

def create_car_title(car_title_dto: Car_TitleDto, db_session: Session):
    car_title = Car_Title(
        car_title=car_title_dto.car_title,
    )

    try:
        db_session.add(car_title)
        db_session.commit()
        db_session.refresh(car_title)
    except Exception as e:
        print(car_title)
    return car_title

def get_car_title(id: int, db_session: Session):
    return db_session.query(Car_Title).filter(Car_Title.id == id).first()

def get_all_car_title(db_session: Session):
    return db_session.query(Car_Title).all()

def update_car_title(id: int, car_title_dto: Car_TitleDto, db_session: Session):

    car_title = db_session.query(Car_Title).filter(Car_Title.id == id).first()
    car_title.car_title = car_title_dto.car_title

    try:
        db_session.add(car_title)
        db_session.commit()
        db_session.refresh(car_title)
    except Exception as e:
        print(car_title)
    return car_title

def delete_car_title(id: int, db_session: Session):
    db_session.query(Car_Title).filter(Car_Title.id == id).delete()
    db_session.commit()
    return

#для модели Car_Model

def create_car_model(car_model_dto: Car_ModelDto, db_session: Session):
    car_model = Car_Model(
        car_model=car_model_dto.car_model,
        car_title_id_id=car_model_dto.car_title_id_id
    )

    try:
        db_session.add(car_model)
        db_session.commit()
        db_session.refresh(car_model)
    except Exception as e:
        print(car_model)
    return car_model

def get_car_model(id: int, db_session: Session):
    return db_session.query(Car_Model).filter(Car_Model.id == id).first()

def get_car_model_by_title(car_title: str, db_session: Session):
    return db_session.query(Car_Model).join(Car_Title).filter(Car_Title.car_title == car_title).all()

def get_all_car_model(db_session: Session):
    return db_session.query(Car_Model).all()

def update_car_model(id: int, car_model_dto: Car_ModelDto, db_session: Session):

    car_model = db_session.query(Car_Model).filter(Car_Model.id == id).first()
    car_model.car_model = car_model_dto.car_model,
    car_model.car_title_id_id = car_model_dto.car_title_id_id

    try:
        db_session.add(car_model)
        db_session.commit()
        db_session.refresh(car_model)
    except Exception as e:
        print(car_model)
    return car_model

def delete_car_model(id: int, db_session: Session):
    db_session.query(Car_Model).filter(Car_Model.id == id).delete()
    db_session.commit()
    return

#для модели Car_Generation

def create_car_generation(car_generation_dto: Car_GenerationDto, db_session: Session):
    car_generation = Car_Generation(
        car_generation=car_generation_dto.car_generation,
        car_model_id_id=car_generation_dto.car_model_id_id
    )

    try:
        db_session.add(car_generation)
        db_session.commit()
        db_session.refresh(car_generation)
    except Exception as e:
        print(car_generation)
    return car_generation

def get_car_generation(id: int, db_session: Session):
    return db_session.query(Car_Generation).filter(Car_Generation.id == id).first()

def get_car_generation_by_model(car_model: str, db_session: Session):
    return db_session.query(Car_Generation).join(Car_Model).filter(Car_Model.car_model == car_model).all()

def get_all_car_generation(db_session: Session):
    return db_session.query(Car_Generation).all()

def update_car_generation(id: int, car_generation_dto: Car_GenerationDto, db_session: Session):

    car_generation = db_session.query(Car_Generation).filter(Car_Generation.id == id).first()
    car_generation.car_generation = car_generation_dto.car_generation,
    car_generation.car_model_id_id = car_generation_dto.car_model_id_id

    try:
        db_session.add(car_generation)
        db_session.commit()
        db_session.refresh(car_generation)
    except Exception as e:
        print(car_generation)
    return car_generation

def delete_car_generation(id: int, db_session: Session):
    db_session.query(Car_Generation).filter(Car_Generation.id == id).delete()
    db_session.commit()
    return

