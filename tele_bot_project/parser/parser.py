
import requests
from bs4 import BeautifulSoup
from datetime import datetime
import psycopg2


class Parser:
    db_name = 'av_by_data_bases'
    user = 'username'
    password = 'your_password'
    host = 'localhost'
    port = '5432'
    #full_url = [f'https://cars.av.by/filter?page={page}' for page in range(1, 121)]
    full_url = [f'https://cars.av.by/filter?brands[0][brand]=6&brands[0][model]=1428&page={page}' for page in range(1, 121)]
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
##############################################################################################

    def create_connection(self):  # подключение к БД
        connection = psycopg2.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.db_name
        )
        return connection

    def create_car_table(self, connection):
        with connection.cursor() as cursor:
            # cursor.execute("""
            # TRUNCATE TABLE tele_bot_app_car
            # """
            # )

            cursor.execute(
                """
                    CREATE TABLE IF NOT EXISTS tele_bot_app_car2
                    (
                        id serial PRIMARY KEY,
                        car_title text,
                        car_model text,
                        car_generation text,
                        car_vin text,
                        main_car_image text,
                        car_images text,
                        year integer,
                        transmission text,
                        engine text,
                        fuel text,
                        car_body text,
                        car_drive text,
                        car_color text,
                        horse_power text,
                        consumption text,
                        mileage integer,
                        price_byn integer,
                        price_usd integer,
                        city text,
                        description text,
                        car_options text,
                        http_link text
                    )

                """
            )
            connection.commit()
            print("Table created successfully")

########################################################################################
    def insert(self, connection, full_data):
        cursor = connection.cursor()
        query = '''INSERT INTO tele_bot_app_car2 (car_title, car_model, car_generation, car_vin, main_car_image,
                        car_images, year, transmission, engine, fuel, car_body, car_drive, car_color, horse_power,
                        consumption, mileage, price_byn, price_usd, city, description, car_options, http_link)
                       VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'''

        for data in full_data:
            values = (data[0], data[1], data[2], data[3], data[4], data[5], int(data[6]), data[7], data[8], data[9],
                      data[10], data[11], data[12], data[13], data[14], int(data[15]), int(data[16]), int(data[17]),
                      data[18], data[19], data[20], data[21])
            cursor.execute(query, values)
        connection.commit()


    def run(self):
        begin_time = datetime.now()
        for link in Parser.full_url:
            car_items = self.get_car_by_link(link)
            print(car_items)
            connection = self.create_connection()
            self.create_car_table(connection)
            self.insert(connection, car_items)

        end_time = datetime.now()
        execute_time = end_time - begin_time
        print(f"Время получения данных {execute_time}")


Parser().run()


