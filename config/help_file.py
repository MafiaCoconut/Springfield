from telebot import types
import os


def create_markup():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    return markup


# TODO: дополнять код при добавлении новых функций в групповой чат
text_help = """
Ниже предоставлены актуальные команды:
================================
Добавление нового предмета
------------------------------------------
/add_eat - Добавление предмета еды
/add_beverages - Добавление предмета напитка
/add_multiple - Добавление расходуемого предмета
/add_one_time - Добавление одноразовой покупки
/add_test - Добавление тестового предмета
/add_subscription - Добавить подписку
================================
Вывод статистики
------------------------------------------
/statistics_all - Вывести всю статистику
/statistics_eat - Вывести статистику еды
/statistics_beverages - Вывести статистику напитков
/statistics_multiple - Вывести статистику расходников
/statistics_one_time - Вывести статистику одноразовых покупок
/statistics_subscription - Вывести статистику подписок
================================
Доп команды
/exit - Выход из добавления предмета
"""


data_of_adding_item = {
    'model': None,
    'title': str,
    'count': str,
    'price': str,
    'payment_date': str
}

this_month = "September"
# this_month = "August"
# this_month = "Juni"
# this_month = "May"
link_database = f"databases/{this_month}.sqlite"

message = None
bot = None


def set_default_values_on_data():
    global data_of_adding_item
    data_of_adding_item = {
        'model': None,
        'title': str,
        'count': int,
        'price': float,
        'payment_data': int
    }
