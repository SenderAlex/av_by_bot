
import requests
from bs4 import BeautifulSoup
from datetime import datetime

from sqlalchemy import create_engine, Column, Integer, String, Text
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Car(Base):
    __tablename__ = 'tele_bot_app_car1'

    id = Column(Integer, primary_key=True)
    car_title = Column(String)
    car_model = Column(String)
    car_generation = Column(String)
    car_vin = Column(String)
    main_car_image = Column(String)
    car_images = Column(Text)
    year = Column(Integer)
    transmission = Column(String)
    engine = Column(String)
    fuel = Column(String)
    car_body = Column(Text)
    car_drive = Column(Text)
    car_color = Column(String)
    horse_power = Column(String)
    consumption = Column(String)
    mileage = Column(Integer)
    price_byn = Column(Integer)
    price_usd = Column(Integer)
    city = Column(String)
    description = Column(Text)
    car_options = Column(Text)
    http_link = Column(String)

engine = create_engine('postgresql://av_by_admin:AVLioneLMessI1024BY@localhost:5432/av_by_data_bases')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)


class Parser:
    #full_url = [f'https://cars.av.by/filter?page={page}' for page in range(1, 121)]
    full_url = [f'https://cars.av.by/filter?brands[0][brand]=5019&page={page}' for page in range(1, 121)]
    #full_url = 'https://api.av.by/offer-types/cars/landings/volkswagen'

    @staticmethod
    def get_car_by_link(link):
        data = []
        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:76.0) Gecko/20100101 Firefox/76.0'}

        response = requests.get(link, headers=headers)
        html = response.text
        html_rating = BeautifulSoup(html, 'html.parser')
        cars = html_rating.find_all('div', class_="listing-item__wrap")
        for car in cars:
            #####
            car_title = ""
            car_model = ""
            car_generation = ""
            car_full_names = car.find_all('span', class_="link-text")
            for car_full_name in car_full_names:
                text_elements = car_full_name.find_all(text=True)
                for text_element in text_elements:
                    text = text_element.strip()
                    if text:
                        if not car_title:
                            car_title = text
                        elif car_title and not car_model:
                            car_model = text
                        elif car_title and car_model and not car_generation:
                            car_generation = text
            ######
            car_vin = "" if car.find_next('div', class_='badge--vin') else "vin"
            image_element = car.find_next('div', class_="listing-item__photo")
            main_car_image = image_element.img['data-src'] if image_element and image_element.img else None  #!!!!!
            car_parameters = car.find_next('div', 'listing-item__params')
            year_div = car_parameters.div
            year = int(year_div.text.replace('г.', ''))
            temporary_data = year_div.find_next_sibling('div')
            temporary_div = temporary_data.text
            temporary_list = temporary_div.split(',')
            transmission = temporary_list[0]
            engine = temporary_list[1].replace('л', '').replace('\xa0', '')
            fuel = temporary_list[2]
            mileage = int(temporary_data.find_next_sibling('div').text.replace('км', '').replace('\u2009', '').
                          replace('\xa0', ''))
            price_byn = int((car.find_next('div', class_="listing-item__price").text.replace('р.', '').
                         replace('\u2009', '').replace('\xa0', '')))
            price_usd = int((car.find_next('div', class_="listing-item__priceusd").text.replace('$', '').
                         replace('≈', '').replace('\u2009', '').replace('\xa0', '')))
            city = car.find_next('div', class_='listing-item__location').text
            message_element = car.find_next('div', class_='listing-item__message')
            description = message_element.text if message_element else None  # !!!!!
            link = car.find_next('a', class_="listing-item__link")
            http_link = f'https://cars.av.by{link["href"]}'

            # проверка существует ли такая ссылка
            existing_link = [item[len(item)-1] for item in data]
            if http_link in existing_link:
                continue

            car_images = []
            car_options = []
            answer = requests.get(http_link, headers=headers)
            htmls = answer.text
            html_answers = BeautifulSoup(htmls, 'html.parser')
            photoes = html_answers.find_all('div', class_='gallery__nav-frame')
            for photo in photoes:
                photo_link = photo.img['data-src'] if photoes else None
                car_images.append(photo_link)

            car_descriptions = html_answers.find_all('div', class_='card__description')
            car_body = ""
            car_drive = ""
            car_color = ""
            for car_description in car_descriptions:
                text_elems = car_description.find_all(text=True)
                for text_elem in text_elems:
                    text_description = text_elem.text.replace(', ', '')
                    if text_description:
                        if not car_body:
                            car_body = text_description
                        elif car_body and not car_drive:
                            car_drive = text_description
                        elif car_body and car_drive and not car_color:
                            car_color = text_description

            car_horsepower_consumption = html_answers.find('div', class_='card__modification')
            horse_power = ""
            consumption = ""
            if car_horsepower_consumption:
                span_element = car_horsepower_consumption.find('span')
                if span_element:
                    car_horse_power_consumption = span_element.text.split('.,')
                    if car_horse_power_consumption:
                        horse_power = car_horse_power_consumption[0]
                        consumption = car_horse_power_consumption[1] if len(car_horse_power_consumption) > 1 else None
            else:
                continue

            car_tag_options = html_answers.find_all('div', 'card__options-section')
            for car_tag_option in car_tag_options:
                category = car_tag_option.find('h4', 'card__options-category').text
                options = car_tag_option.find('ul', 'card__options-list').find_all('li')
                options_list = [option.text for option in options]
                options_list_comma = ', '.join(options_list)
                car_options.append(f'{category}: {options_list_comma}')
            data.append(
                (car_title, car_model, car_generation, car_vin, main_car_image, car_images, year, transmission,
                 engine, fuel, car_body, car_drive, car_color, horse_power, consumption, mileage, price_byn,
                 price_usd, city, description, car_options, http_link)
            )
            print(f" ")
            print(f"{car_title} -- {car_model} -- {car_generation} -- {car_vin} -- {main_car_image} -- {car_images} --"
                  f"{year} -- {transmission} -- {engine} -- {fuel} -- {car_body} -- {car_drive} -- {car_color} --"
                  f"{horse_power} -- {consumption} -- {mileage} -- {price_byn} -- {price_usd} -- {city} --"
                  f"{description} -- {car_options} -- {http_link}")

        return data
########################
    def create_connection(self):  # подключение к БД
        return Session()

#########################
    def insert(self, session, full_data):
        for data in full_data:
            car = Car(**{
                'car_title': data[0],
                'car_model': data[1],
                'car_generation': data[2],
                'car_vin': data[3],
                'main_car_image': data[4],
                'car_images': data[5],
                'year': data[6],
                'transmission': data[7],
                'engine': data[8],
                'fuel': data[9],
                'car_body': data[10],
                'car_drive': data[11],
                'car_color': data[12],
                'horse_power': data[13],
                'consumption': data[14],
                'mileage': data[15],
                'price_byn': data[16],
                'price_usd': data[17],
                'city': data[18],
                'description': data[19],
                'car_options': data[20],
                'http_link': data[21],
            })
            session.add(car)

        session.commit()


    def run(self):
        begin_time = datetime.now()
        session = self.create_connection()
        for link in Parser.full_url:
            car_items = self.get_car_by_link(link)
            print(car_items)
            self.insert(session, car_items)

        end_time = datetime.now()
        execute_time = end_time - begin_time
        print(f"Время получения данных {execute_time}")


Parser().run()


