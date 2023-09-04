import uuid
from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class Thing:
    id: uuid.UUID = field(default_factory=uuid.uuid4)
    title: str = field(default="")
    count: int = field(default="")
    price: float = field(default=0.0)
    created: datetime.now = field(default=datetime.now())


@dataclass
class Eat(Thing):
    table = 'eat'
    name = "Еда"


@dataclass
class Beverages(Thing):
    table = 'beverages'
    name = "Напитки"


@dataclass
class MultiplePurchase(Thing):
    table = 'multiple_purchase'
    name = "Многоразовые покупки"


@dataclass
class OneTimePurchase(Thing):
    table = 'one_time_purchase'
    name = "Одноразовые покупки"


@dataclass
class Test(Thing):
    table = 'test'
    name = "Тест"


@dataclass
class MonthlyPayment:
    id: uuid.UUID = field(default_factory=uuid.uuid4)
    title: str = field(default="")
    price: float = field(default=0.0)
    payment_date: int = field(default=0)


@dataclass
class Subscription(MonthlyPayment):
    created: datetime.now = field(default=datetime.now())
    table = "subscription"
    name = "Подписки"


@dataclass
class RegularExpenses(MonthlyPayment):
    table = "regular_expenses"
    name = "Регулярные расходы"


# TODO создать таблицу для "другое"