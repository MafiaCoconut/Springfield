import sqlite3
from models.data_classes import Thing, Eat, Beverages, MultiplePurchase, OneTimePurchase, Test
from dataclasses import asdict, astuple, dataclass
from config import help_file as hp
from config.log_def import *

status = "debug"
tag = "SQLite"
data_class = Thing
models = [Eat, Beverages, MultiplePurchase, OneTimePurchase, Test]
map_model = {
    1: Eat,
    2: Beverages,
    3: MultiplePurchase,
    4: OneTimePurchase,
    5: Test
}


class SQLite:
    def __init__(self, connection):
        self.connection = connection
        self.cursor = self.connection.cursor()
        self.list_of_things = {
            'eat': [], 'beverages': [], 'multiple_purchase': [], 'one_time_purchase': [], 'test': [], 'every_month': [],
        }

    def save_thing(self):
        function_name = "send_data"
        set_func(function_name, tag, status)

        set_inside_func(f"Предмет: {hp.data_of_adding_item['title']}, "
                        f"Кол-во: {hp.data_of_adding_item['count']}, "
                        f"Цена: {hp.data_of_adding_item['price']}", function_name, tag)

        model = hp.data_of_adding_item['model'](title=hp.data_of_adding_item['title'],
                                                count=hp.data_of_adding_item['count'],
                                                price=hp.data_of_adding_item['price'])

        args = [str(model.id), model.title, model.count, model.price, model.created]
        sqlite_insert_query = f"""INSERT INTO {model.table}
                                 (id, title, count, price, created)
                                 VALUES (?, ?, ?, ?, ?);"""

        self.cursor.execute(sqlite_insert_query, args)
        self.connection.commit()

    def save_subscription(self):
        function_name = "save_thing"
        set_func(function_name, tag, status)

        set_inside_func(f"Предмет: {hp.data_of_adding_item['title']}, "
                        f"Цена: {hp.data_of_adding_item['price']}, "
                        f"Дата оплаты: {hp.data_of_adding_item['payment_date']}", function_name, tag)

        model = hp.data_of_adding_item['model'](title=hp.data_of_adding_item['title'],
                                                price=hp.data_of_adding_item['price'],
                                                payment_date=hp.data_of_adding_item['payment_date'])

        args = [str(model.id), model.title, model.price, model.payment_date, model.created]
        sqlite_insert_query = f"""INSERT INTO {model.table}
                                 (id, title, price, payment_date, created)
                                 VALUES (?, ?, ?, ?, ?);"""

        self.cursor.execute(sqlite_insert_query, args)
        self.connection.commit()

    def create_bd(self, model):
        function_name = "create_bd"
        set_func(function_name, tag, status)

        self.cursor.execute(f"""
        CREATE TABLE IF NOT EXISTS {model.table} (
        id uuid PRIMARY KEY,
        title TEXT NOT NULL,
        count Text,
        price TEXT,
        created timestamp with time zone
        );""")
        self.connection.commit()

    def delete_bd(self, model):
        function_name = "delete_bd"
        set_func(function_name, tag, status)

        self.cursor.execute(f"""DELETE FROM {model.table};""")
        self.connection.commit()

    def get_bd(self, model):
        function_name = "get_bd"
        set_func(function_name, tag, status)

        self.cursor.execute(f"""SELECT * FROM {model.table};""")
        data = self.cursor.fetchall()
        self.connection.commit()
        return data
