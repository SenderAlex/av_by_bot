from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from dotenv import load_dotenv
import os

load_dotenv()
host = os.getenv('IP')
user = str(os.getenv('POSTGRES_USER'))
password = str(os.getenv('POSTGRES_PASSWORD'))
database = str(os.getenv('POSTGRES_DATABASE'))

POSTGRES_URI = f'postgresql+psycopg2://{user}:{password}@{host}/{database}'
print(f"{POSTGRES_URI=}")

engine = create_engine(POSTGRES_URI)  # движок нашей БД (создается engine, подрубается наша БД по указанному url)
session = sessionmaker(autoflush=False, autocommit=False, bind=engine)
Base = declarative_base()  # создаем нашу БД, объявляем нашу БД


def get_session():  # функция, которая, позволяет получить нашу БД
    db = session()
    try:
        yield db
    finally:
        db.close()