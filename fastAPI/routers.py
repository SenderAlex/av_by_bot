
import json
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_session
from Services import (services_car, services_car_body, services_car_drive, services_car_engine,
services_car_engine_type, services_car_registration, services_car_title_model_generation,
services_car_transmission, services_car_year)

from DTO.dto_car import CarDto
from DTO.dto_car_title_model_generation import Car_TitleDto, Car_ModelDto, Car_GenerationDto
from DTO.dto_car_year import Car_YearDto
from DTO.dto_car_engine import Car_EngineDto
from DTO.dto_car_transmission import Car_TransmissionDto
from DTO.dto_car_body import Car_BodyDto
from DTO.dto_car_engine_type import Car_EngineTypeDto
from DTO.dto_car_drive import Car_DriveDto
from DTO.dto_car_registration import Car_RegistrationDto
from DTO.dto_car_authentification import LoginRequest, LoginResponse


from Models.models_car_registration import Car_Registration

router = APIRouter()

# Car
@router.post('/car', tags=["car"])  # что значит команды с @?
async def create(car_dto: CarDto = None, db_session: Session = Depends(get_session)):  # С этим разобраться!!!
    return services_car.create_car(car_dto, db_session)

@router.get('/car/{id}', tags=["car"])
async def get(car_id: int, db_session: Session = Depends(get_session)):  # С этим разобраться!!!
    return services_car.get_car(car_id, db_session)

@router.get('/cars', tags=["car"])
async def get_all(db_session: Session = Depends(get_session)):  # С этим разобраться!!!
    return services_car.get_all_car(db_session)

@router.put('/car/{id}', tags=["car"])
async def update(car_id: int, car_dto: CarDto = None, db_session: Session = Depends(get_session)):  # С этим разобраться!!!
    return services_car.update_car(car_id, car_dto, db_session)

@router.delete('/car/{id}', tags=["car"])
async def delete(car_id: int, db_session: Session = Depends(get_session)):  # С этим разобраться!!!
    return services_car.delete_car(car_id, db_session)

# Car_Title
@router.post('/car_title', tags=["car_title"])  # что значит команды с @?
async def create(car_title_dto: Car_TitleDto = None, db_session: Session = Depends(get_session)):  # С этим разобраться!!!
    return services_car_title_model_generation.create_car_title(car_title_dto, db_session)

@router.get('/car_title/{id}', tags=["car_title"])
async def get(car_title_id: int, db_session: Session = Depends(get_session)):  # С этим разобраться!!!
    return services_car_title_model_generation.get_car_title(car_title_id, db_session)

@router.get('/car_titles', tags=["car_title"])
async def get_all(db_session: Session = Depends(get_session)):  # С этим разобраться!!!
    return services_car_title_model_generation.get_all_car_title(db_session)

@router.put('/car_title/{id}', tags=["car_title"])
async def update(car_title_id: int, car_title_dto: Car_TitleDto = None, db_session: Session = Depends(get_session)):  # С этим разобраться!!!
    return services_car_title_model_generation.update_car_title(car_title_id, car_title_dto, db_session)

@router.delete('/car_title/{id}', tags=["car_title"])
async def delete(car_title_id: int, db_session: Session = Depends(get_session)):  # С этим разобраться!!!
    return services_car_title_model_generation.delete_car_title(car_title_id, db_session)

# Car_Model
@router.post('/car_model', tags=["car_model"])  # что значит команды с @?
async def create(car_model_dto: Car_ModelDto = None, db_session: Session = Depends(get_session)):  # С этим разобраться!!!
    return services_car_title_model_generation.create_car_model(car_model_dto, db_session)

@router.get('/car_model/{id}', tags=["car_model"])
async def get(car_model_id: int, db_session: Session = Depends(get_session)):  # С этим разобраться!!!
    return services_car_title_model_generation.get_car_model(car_model_id, db_session)

@router.get('/car_models/car_models_by_title/', tags=["car_model"])
async def get(car_title: str, db_session: Session = Depends(get_session)):  # С этим разобраться!!!
    return services_car_title_model_generation.get_car_model_by_title(car_title, db_session)

@router.get('/car_models', tags=["car_model"])
async def get_all(db_session: Session = Depends(get_session)):  # С этим разобраться!!!
    return services_car_title_model_generation.get_all_car_model(db_session)

@router.put('/car_model/{id}', tags=["car_model"])
async def update(car_model_id: int, car_model_dto: Car_ModelDto = None, db_session: Session = Depends(get_session)):  # С этим разобраться!!!
    return services_car_title_model_generation.update_car_model(car_model_id, car_model_dto, db_session)

@router.delete('/car_model/{id}', tags=["car_model"])
async def delete(car_model_id: int, db_session: Session = Depends(get_session)):  # С этим разобраться!!!
    return services_car_title_model_generation.delete_car_model(car_model_id, db_session)


# Car_Generation
@router.post('/car_generation', tags=["car_generation"])  # что значит команды с @?
async def create(car_generation_dto: Car_GenerationDto = None, db_session: Session = Depends(get_session)):  # С этим разобраться!!!
    return services_car_title_model_generation.create_car_generation(car_generation_dto, db_session)

@router.get('/car_generation/{id}', tags=["car_generation"])
async def get(car_generation_id: int, db_session: Session = Depends(get_session)):  # С этим разобраться!!!
    return services_car_title_model_generation.get_car_generation(car_generation_id, db_session)

@router.get('/car_generations/car_generations_by_model/', tags=["car_generation"])
async def get(car_model: str, db_session: Session = Depends(get_session)):  # С этим разобраться!!!
    return services_car_title_model_generation.get_car_generation_by_model(car_model, db_session)

@router.get('/car_generations', tags=["car_generation"])
async def get_all(db_session: Session = Depends(get_session)):  # С этим разобраться!!!
    return services_car_title_model_generation.get_all_car_generation(db_session)

@router.put('/car_generation/{id}', tags=["car_generation"])
async def update(car_generation_id: int, car_generation_dto: Car_ModelDto = None, db_session: Session = Depends(get_session)):  # С этим разобраться!!!
    return services_car_title_model_generation.update_car_model(car_generation_id, car_generation_dto, db_session)

@router.delete('/car_generation/{id}', tags=["car_generation"])
async def delete(car_generation_id: int, db_session: Session = Depends(get_session)):  # С этим разобраться!!!
    return services_car_title_model_generation.delete_car_title(car_generation_id, db_session)

# Car_Year
@router.post('/car_year', tags=["car_year"])  # что значит команды с @?
async def create(car_year_dto: Car_YearDto = None, db_session: Session = Depends(get_session)):  # С этим разобраться!!!
    return services_car_year.create_car_year(car_year_dto, db_session)

@router.get('/car_year/{id}', tags=["car_year"])
async def get(car_year_id: int, db_session: Session = Depends(get_session)):  # С этим разобраться!!!
    return services_car_year.get_car_year(car_year_id, db_session)

@router.get('/car_years', tags=["car_year"])
async def get_all(db_session: Session = Depends(get_session)):  # С этим разобраться!!!
    return services_car_year.get_all_car_year(db_session)

@router.put('/car_year/{id}', tags=["car_year"])
async def update(car_year_id: int, car_year_dto: Car_YearDto = None, db_session: Session = Depends(get_session)):  # С этим разобраться!!!
    return services_car_year.update_car_year(car_year_id, car_year_dto, db_session)

@router.delete('/car_year/{id}', tags=["car_year"])
async def delete(car_year_id: int, db_session: Session = Depends(get_session)):  # С этим разобраться!!!
    return services_car_year.delete_car_year(car_year_id, db_session)

# Car_Engine
@router.post('/car_engine', tags=["car_engine"])  # что значит команды с @?
async def create(car_engine_dto: Car_EngineDto = None, db_session: Session = Depends(get_session)):  # С этим разобраться!!!
    return services_car_engine.create_car_engine(car_engine_dto, db_session)

@router.get('/car_engine/{id}', tags=["car_engine"])
async def get(car_engine_id: int, db_session: Session = Depends(get_session)):  # С этим разобраться!!!
    return services_car_engine.get_car_engine(car_engine_id, db_session)

@router.get('/car_engines', tags=["car_engine"])
async def get_all(db_session: Session = Depends(get_session)):  # С этим разобраться!!!
    return services_car_engine.get_all_car_engine(db_session)

@router.put('/car_engine/{id}', tags=["car_engine"])
async def update(car_engine_id: int, car_engine_dto: Car_EngineDto = None, db_session: Session = Depends(get_session)):  # С этим разобраться!!!
    return services_car_engine.update_car_engine(car_engine_id, car_engine_dto, db_session)

@router.delete('/car_engine/{id}', tags=["car_engine"])
async def delete(car_engine_id: int, db_session: Session = Depends(get_session)):  # С этим разобраться!!!
    return services_car_engine.delete_car_engine(car_engine_id, db_session)

# Car_Transmission
@router.post('/car_transmission', tags=["car_transmission"])  # что значит команды с @?
async def create(car_transmission_dto: Car_TransmissionDto = None, db_session: Session = Depends(get_session)):  # С этим разобраться!!!
    return services_car_transmission.create_car_transmission(car_transmission_dto, db_session)

@router.get('/car_transmission/{id}', tags=["car_transmission"])
async def get(car_transmission_id: int, db_session: Session = Depends(get_session)):  # С этим разобраться!!!
    return services_car_transmission.get_car_transmission(car_transmission_id, db_session)

@router.get('/car_transmissions', tags=["car_transmission"])
async def get_all(db_session: Session = Depends(get_session)):  # С этим разобраться!!!
    return services_car_transmission.get_all_car_transmission(db_session)

@router.put('/car_transmission/{id}', tags=["car_transmission"])
async def update(car_transmission_id: int, car_transmission_dto: Car_TransmissionDto = None, db_session: Session = Depends(get_session)):  # С этим разобраться!!!
    return services_car_transmission.update_car_transmission(car_transmission_id, car_transmission_dto, db_session)

@router.delete('/car_transmission/{id}', tags=["car_transmission"])
async def delete(car_transmission_id: int, db_session: Session = Depends(get_session)):  # С этим разобраться!!!
    return services_car_transmission.delete_car_transmission(car_transmission_id, db_session)

# Car_Body
@router.post('/car_body', tags=["car_body"])  # что значит команды с @?
async def create(car_body_dto: Car_BodyDto = None, db_session: Session = Depends(get_session)):  # С этим разобраться!!!
    return services_car_body.create_car_body(car_body_dto, db_session)

@router.get('/car_body/{id}', tags=["car_body"])
async def get(car_body_id: int, db_session: Session = Depends(get_session)):  # С этим разобраться!!!
    return services_car_body.get_car_body(car_body_id, db_session)

@router.get('/car_bodies', tags=["car_body"])
async def get_all(db_session: Session = Depends(get_session)):  # С этим разобраться!!!
    return services_car_body.get_all_car_body(db_session)

@router.put('/car_body/{id}', tags=["car_body"])
async def update(car_body_id: int, car_body_dto: Car_BodyDto = None, db_session: Session = Depends(get_session)):  # С этим разобраться!!!
    return services_car_body.update_car_body(car_body_id, car_body_dto, db_session)

@router.delete('/car_body/{id}', tags=["car_body"])
async def delete(car_body_id: int, db_session: Session = Depends(get_session)):  # С этим разобраться!!!
    return services_car_body.delete_car_body(car_body_id, db_session)

# Car_EngineType
@router.post('/car_engine_type', tags=["car_engine_type"])  # что значит команды с @?
async def create(car_engine_type_dto: Car_EngineTypeDto = None, db_session: Session = Depends(get_session)):  # С этим разобраться!!!
    return services_car_engine_type.create_car_engine_type(car_engine_type_dto, db_session)

@router.get('/car_engine_type/{id}', tags=["car_engine_type"])
async def get(car_engine_type_id: int, db_session: Session = Depends(get_session)):  # С этим разобраться!!!
    return services_car_engine_type.get_car_engine_type(car_engine_type_id, db_session)

@router.get('/car_engine_types', tags=["car_engine_type"])
async def get_all(db_session: Session = Depends(get_session)):  # С этим разобраться!!!
    return services_car_engine_type.get_all_car_engine_type(db_session)

@router.put('/car_engine_type/{id}', tags=["car_engine_type"])
async def update(car_engine_type_id: int, car_engine_type_dto: Car_EngineTypeDto = None, db_session: Session = Depends(get_session)):  # С этим разобраться!!!
    return services_car_engine_type.update_car_engine_type(car_engine_type_id, car_engine_type_dto, db_session)

@router.delete('/car_engine_type/{id}', tags=["car_engine_type"])
async def delete(car_engine_type_id: int, db_session: Session = Depends(get_session)):  # С этим разобраться!!!
    return services_car_engine_type.delete_car_engine_type(car_engine_type_id, db_session)

# Car_Drive
@router.post('/car_drive', tags=["car_drive"])  # что значит команды с @?
async def create(car_drive_dto: Car_DriveDto = None, db_session: Session = Depends(get_session)):  # С этим разобраться!!!
    return services_car_drive.create_car_drive(car_drive_dto, db_session)

@router.get('/car_drive/{id}', tags=["car_drive"])
async def get(car_drive_id: int, db_session: Session = Depends(get_session)):  # С этим разобраться!!!
    return services_car_drive.get_car_drive(car_drive_id, db_session)

@router.get('/car_drives', tags=["car_drive"])
async def get_all(db_session: Session = Depends(get_session)):  # С этим разобраться!!!
    return services_car_drive.get_all_car_drive(db_session)

@router.put('/car_drive/{id}', tags=["car_drive"])
async def update(car_drive_id: int, car_drive_dto: Car_DriveDto = None, db_session: Session = Depends(get_session)):  # С этим разобраться!!!
    return services_car_drive.update_car_drive(car_drive_id, car_drive_dto, db_session)

@router.delete('/car_drive/{id}', tags=["car_drive"])
async def delete(car_drive_id: int, db_session: Session = Depends(get_session)):  # С этим разобраться!!!
    return services_car_drive.delete_car_drive(car_drive_id, db_session)

# Car_Registration
@router.post('/car_registration', tags=["car_registration"])  # что значит команды с @?
async def create(car_registration_dto: Car_RegistrationDto = None, db_session: Session = Depends(get_session)):  # С этим разобраться!!!
    return services_car_registration.create_car_registration(car_registration_dto, db_session)

@router.get('/car_registration/{id}', tags=["car_registration"])
async def get(car_registration_id: int, db_session: Session = Depends(get_session)):  # С этим разобраться!!!
    return services_car_registration.get_car_registration(car_registration_id, db_session)

@router.get('/car_registrations', tags=["car_registration"])
async def get_all(db_session: Session = Depends(get_session)):  # С этим разобраться!!!
    return services_car_registration.get_all_car_registration(db_session)

@router.put('/car_registration/{id}', tags=["car_registration"])
async def update(car_registration_id: int, car_registration_dto: Car_RegistrationDto = None, db_session: Session = Depends(get_session)):  # С этим разобраться!!!
    return services_car_registration.update_car_registration(car_registration_id, car_registration_dto, db_session)

@router.delete('/car_registration/{id}', tags=["car_registration"])
async def delete(car_registration_id: int, db_session: Session = Depends(get_session)):  # С этим разобраться!!!
    return services_car_registration.delete_car_registration(car_registration_id, db_session)


#Registration
# @router.post('/car_registration', tags=["car_registration"], response_model=None)
# def registration(body: Car_RegistrationDto, db_session: Depends(get_session)):
#     existing_user = db_session.query(Car_Registration).filter(Car_Registration.username == body.username,
#         Car_Registration.email == body.email, Car_Registration.password == body.password).first()
#     if existing_user:
#         return {'message': "Такой пользователь уже существует"}
#
#     new_user = Car_Registration(username=body.username, email=body.email, password=body.password)
#     db_session.add(new_user)
#     db_session.commit()
#
#     return {'message': "Пользователь успешно зарегистрирован"}


#Car_ValidatedData
@router.post('/login', tags=["login"], response_model=LoginResponse)
def login(email: str, password: str, db_session: Session = Depends(get_session)):
    user = db_session.query(Car_Registration).filter_by(Car_Registration.email == email,
                                                        Car_Registration.password == password).first()

# def login (credentials: LoginResponse, db_session: Session=Depends()):
#     user = db_session.query(Car_Registration).filter(Car_Registration.email == credentials.email,
#                                                      Car_Registration.password == credentials.password).first()

    if user:
        return {'message': 'Вы зашли в свой личный кабинет!', 'session': json.loads(json.dumps(db_session, default=str))}
    else:
        raise HTTPException(status_code=401, detail='Неверные данные для входа')








# from fastapi import APIRouter
#
# router = APIRouter()

