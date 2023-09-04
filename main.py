import telebot
from config import settings
from models.SQLte import SQLite
from config.log_def import *
import config.help_file as hp
from models.data_classes import Eat, Beverages, MultiplePurchase, OneTimePurchase, Test, Subscription, RegularExpenses
import sqlite3
# from handlers.statistics import statistic_all, statistics_subscription, statistic_thing

status = "debug"
# bot = telebot.TeleBot(env.  TOKEN)
bot = telebot.TeleBot('1388041899:AAHGlacG8iak0AFCTu5ULyAZ8inRQA2rP4g')
models = [Eat, Beverages, MultiplePurchase, OneTimePurchase]
tag = "main"
map_model = {
    1: Eat,
    2: Beverages,
    3: MultiplePurchase,
    4: OneTimePurchase,
    # 5: Test,
    6: Subscription
}


# @bot.message_handler(commands=['statistics_all', 'statistics_subscription', 'statistics_eat', 'statistics_beverages',
#                                'statistics_multiple', 'statistics_one_time'])
# def statistics(message):
#     function_name = "statistics"
#     set_func(function_name, tag, status)
#
#     hp.message = message
#
#     if message.text[12:] == "all":
#         statistic_all()
#     elif message.text[12:] == "subscription":
#         statistics_subscription()
#     elif message.text[12:] == "eat":
#         statistic_thing(Eat)
#     elif message.text[12:] == "beverages":
#         statistic_thing(Beverages)
#     elif message.text[12:] == "multiple":
#         statistic_thing(MultiplePurchase)
#     elif message.text[12:] == "one_time":
#         statistic_thing(OneTimePurchase)
#
#
# @bot.message_handler(commands=['add_eat', 'add_beverages', 'add_multiple',
#                                'add_one_time', 'add_test', 'add_subscription'])
# def add_item(message):
#     function_name = "add_item"
#     set_func(function_name, tag, status)
#
#     model = ""
#     type_of_item = ""
#     if message.text[5:] == "eat":
#         hp.data_of_adding_item['model'] = Eat
#         model = "еды"
#         type_of_item = "thing"
#     elif message.text[5:] == "beverages":
#         hp.data_of_adding_item['model'] = Beverages
#         model = "напитка"
#         type_of_item = "thing"
#     elif message.text[5:] == "multiple":
#         hp.data_of_adding_item['model'] = MultiplePurchase
#         model = 'многоразового предмета'
#         type_of_item = "thing"
#     elif message.text[5:] == "one_time":
#         hp.data_of_adding_item['model'] = OneTimePurchase
#         model = "одноразовой покупки"
#         type_of_item = "thing"
#     elif message.text[5:] == "test":
#         hp.data_of_adding_item['model'] = Test
#         model = "тестового предмета"
#         type_of_item = "thing"
#     elif message.text[5:] == "one_time":
#         hp.data_of_adding_item['model'] = Subscription
#         model = "подписки"
#         type_of_item = "subscription"
#
#     bot.send_message(message.chat.id, f"Активировано добавление {model}")
#
#     if type_of_item == "thing":
#         bot.register_next_step_handler(message, set_title)
#     elif type_of_item == "subscription":
#         bot.register_next_step_handler(message, set_title)
#
#
# @bot.message_handler(commands=["help"])
# def help_function(message):
#     function_name = "help_function"
#     set_func(function_name, tag, status)
#
#     bot.send_message(message.chat.id, hp.text_help)
#
#
# def set_title(message):
#     function_name = "set_title"
#     set_func(function_name, tag, status)
#
#     if message.text != "/exit":
#         hp.data_of_adding_item['title'] = message.text
#         if hp.data_of_adding_item['model'] == Subscription:
#             bot.register_next_step_handler(message, set_price)
#         else:
#             bot.register_next_step_handler(message, set_count)
#     else:
#         bot.send_message(message.chat.id, "Добавление предмета остановлено")
#         hp.set_default_values_on_data()
#
#
# def set_count(message):
#     function_name = "set_count"
#     set_func(function_name, tag, status)
#
#     if message.text != "/exit":
#         try:
#             result = int(message.text)
#             hp.data_of_adding_item['count'] = result
#             bot.register_next_step_handler(message, set_price)
#         except:
#             bot.send_message(message.chat.id, "Повторите ввод данных")
#             bot.register_next_step_handler(message, set_count)
#     else:
#         bot.send_message(message.chat.id, "Добавление предмета остановлено")
#         hp.set_default_values_on_data()
#
#
# def set_price(message):
#     function_name = "set_price"
#     set_func(function_name, tag, status)
#
#     if message.text != "/exit":
#         try:
#             text = message.text
#             result = float(text.replace(',', '.'))
#             hp.data_of_adding_item['price'] = result
#
#             if hp.data_of_adding_item['model'] == Subscription:
#                 set_inside_func("успешно обработано условие", function_name, tag)
#                 bot.register_next_step_handler(message, set_payment_data)
#             else:
#                 save_item(message)
#         except:
#             bot.send_message(message.chat.id, "Повторите ввод данных")
#             bot.register_next_step_handler(message, set_price)
#     else:
#         bot.send_message(message.chat.id, "Добавление предмета остановлено")
#         hp.set_default_values_on_data()
#
#
# def set_payment_data(message):
#     function_name = "set_payment_data"
#     set_func(function_name, tag, status)
#
#     if message.text != "/exit":
#         try:
#             result = int(message.text)
#             hp.data_of_adding_item['payment_date'] = result
#             set_inside_func(hp.data_of_adding_item, function_name, tag)
#
#             save_item(message)
#         except:
#             bot.send_message(message.chat.id, "Повторите ввод данных")
#             bot.register_next_step_handler(message, set_payment_data)
#     else:
#         bot.send_message(message.chat.id, "Добавление предмета остановлено")
#         hp.set_default_values_on_data()
#
#
# def save_item(message):
#     function_name = "save_item"
#     set_func(function_name, tag, status)
#
#     with sqlite3.connect(hp.link_database) as sqlite_conn:
#         sqlite_model = SQLite(sqlite_conn)
#
#         if hp.data_of_adding_item['model'] == Subscription:
#             bot.send_message(message.chat.id, f"Предмет: {hp.data_of_adding_item['title']}, "
#                                               f"Цена: {hp.data_of_adding_item['price']}, "
#                                               f"Дата оплаты: {hp.data_of_adding_item['payment_date']}")
#             sqlite_model.save_subscription()
#         else:
#             bot.send_message(message.chat.id, f"Предмет: {hp.data_of_adding_item['title']}, "
#                                               f"Кол-во: {hp.data_of_adding_item['count']}, "
#                                               f"Цена: {hp.data_of_adding_item['price']}")
#             sqlite_model.save_thing()
#
#     hp.set_default_values_on_data()


if __name__ == '__main__':
    try:
        settings.main()
        hp.bot = bot
        # bot.polling(none_stop=True, timeout=3000000)
        bot.polling(none_stop=True)
    except:
        pass