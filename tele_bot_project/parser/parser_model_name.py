
import requests
from bs4 import BeautifulSoup
from datetime import datetime
import psycopg2


class Parser:
    db_name = 'av_by_data_bases'
    user = 'av_by_admin'
    password = 'AVLioneLMessI1024BY'
    host = 'localhost'
    port = '5432'
    #car_title_url = f'https://cars.av.by/'
    #car_title_url = f'https://av.by/catalog'

    @staticmethod
    def get_car_title_by_link():
        #data = []
        title_data = []
        #headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:76.0) Gecko/20100101 Firefox/76.0'}

        with open('title.html', 'r', encoding='utf-8') as file:
            html_content = file.read()
        html_rating = BeautifulSoup(html_content, 'html.parser')

        car_titles = [span.text for span in html_rating.select('div.catalog__list span.catalog__title')]

        for car_title in car_titles:
            title_data.append(car_title)
        return title_data

    @staticmethod
    def get_model_title(title):
        model_data = []
        auto_title = title.replace(' ', '-').replace(', ', '-').lower()
        car_model_url = f'https://av.by/catalog/{auto_title}'
        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:76.0) Gecko/20100101 Firefox/76.0'}

        response = requests.get(car_model_url, headers=headers)
        html = response.text
        html_rating = BeautifulSoup(html, 'html.parser')
        car_models = html_rating.find_all('li', class_='catalog__item')
        for car_model in car_models:
            model = car_model.text
            model_data.append(model)
        return model_data

    @staticmethod
    def get_generation_title(title, model):
        generation_data = []
        auto_title = title.replace(' ', '-').replace(', ', '-').lower()
        auto_model = model.replace(' ', '-').replace(', ', '-').lower()
        car_model_url = f'https://av.by/catalog/{auto_title}_{auto_model}'
        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:76.0) Gecko/20100101 Firefox/76.0'}

        response = requests.get(car_model_url, headers=headers)
        html = response.text
        html_rating = BeautifulSoup(html, 'html.parser')
        car_generations = html_rating.find_all('div', class_='generations__title')
        for car_generation in car_generations:
            generation = car_generation.text
            generation_data.append(generation)
        return generation_data

##############################################################################################

    def create_connection(self):  # подключение к БД
        connection = psycopg2.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.db_name
        )
        return connection

    def create_car_title_table(self, connection):
        with connection.cursor() as cursor:
            # cursor.execute("""
            # TRUNCATE TABLE tele_bot_app_car
            # """
            # )

            cursor.execute(
                """
                    CREATE TABLE IF NOT EXISTS tele_bot_app_car_title1
                    (
                        id serial PRIMARY KEY,
                        car_title text
                    )

                """
            )
            connection.commit()
            print("Table created successfully")

    def create_car_model_table(self, connection):
        with connection.cursor() as cursor:
            # cursor.execute("""
            # TRUNCATE TABLE tele_bot_app_car
            # """
            # )

            cursor.execute(
                """
                    CREATE TABLE IF NOT EXISTS tele_bot_app_car_model1
                    (
                        id serial PRIMARY KEY,
                        car_model text,
                        car_title_id_id INT,
                        FOREIGN KEY (car_title_id_id) REFERENCES tele_bot_app_car_title1 (id)
                    )

                """
            )
            connection.commit()
            print("Table created successfully")

    def create_car_generation_table(self, connection):
        with connection.cursor() as cursor:
            # cursor.execute("""
            # TRUNCATE TABLE tele_bot_app_car
            # """
            # )

            cursor.execute(
                """
                    CREATE TABLE IF NOT EXISTS tele_bot_app_car_generation1
                    (
                        id serial PRIMARY KEY,
                        car_generation text,
                        car_model_id_id INT,
                        FOREIGN KEY (car_model_id_id) REFERENCES tele_bot_app_car_model1 (id)
                    )

                """
            )
            connection.commit()
            print("Table created successfully")

########################################################################################
    def insert_into_car_title(self, connection, title):
        cursor = connection.cursor()
        query = '''INSERT INTO tele_bot_app_car_title1 (car_title) VALUES (%s)'''

        values = (title,)
        cursor.execute(query, values)
        connection.commit()

    def insert_into_car_model(self, connection, car_title_id_id, model):
        cursor = connection.cursor()
        query = '''INSERT INTO tele_bot_app_car_model1 (car_model, car_title_id_id) VALUES (%s, %s)'''

        values = (model, car_title_id_id)
        cursor.execute(query, values)
        connection.commit()

    def insert_into_car_generation(self, connection, car_model_id_id, generation):
        cursor = connection.cursor()
        query = '''INSERT INTO tele_bot_app_car_generation1 (car_generation, car_model_id_id) VALUES (%s, %s)'''

        values = (generation, car_model_id_id)
        cursor.execute(query, values)
        connection.commit()


    def run(self):
        title_data = []
        model_data = []
        generation_data = []
        begin_time = datetime.now()

        connection = self.create_connection()
        self.create_car_title_table(connection)
        self.create_car_model_table(connection)
        self.create_car_generation_table(connection)

        car_titles = self.get_car_title_by_link()
        for title_number, car_title in enumerate(car_titles):
            title_data.append(car_title)
            title = str(title_data[-1])
            self.insert_into_car_title(connection, title)

            car_models = self.get_model_title(car_title)
            for model_number, car_model in enumerate(car_models):
                model_data.append(car_model)
                model = str(model_data[-1])
                self.insert_into_car_model(connection, len(title_data), model)

                car_generations = self.get_generation_title(title, model)
                for car_generation in car_generations:
                    generation_data.append(car_generation)
                    generation = str(generation_data[-1])
                    self.insert_into_car_generation(connection, len(model_data), generation)

        print(title_data)
        print(model_data)
        print(generation_data)

        end_time = datetime.now()
        execute_time = end_time - begin_time
        print(f"Время получения данных {execute_time}")

Parser().run()


