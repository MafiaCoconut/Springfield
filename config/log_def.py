import logging


def set_func(function, tag, status="info"):
    if status == "info":
        logging.info(f"[%s] Вызвана функция: {function}", tag)
    elif status == "debug":
        logging.debug(f"[%s] Вызвана функция: {function}", tag)


def set_func_and_person(function, tag, message, status="info"):
    if status == "info":
        logging.info(f"[%s] Вызвана функция: ({function}) пользователем: @{message.from_user.username}", tag)
    elif status == "debug":
        logging.debug(f"[%s] Вызвана функция: ({function}) пользователем: @{message.from_user.username}", tag)


def set_inside_func(data, function, tag, status="info"):
    if status == "info":
        logging.info(f"[%s] [%s]: {data}", tag, function)
    elif status == "debug":
        logging.debug(f"[%s] [%s]: {data}", tag, function)
