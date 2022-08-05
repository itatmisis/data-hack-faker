from dataclasses import dataclass, field
import datetime
import random

from faker import Faker

fake_ru = Faker(locale="ru_RU")


@dataclass
class Person:
    first_name: str
    last_name: str
    age: int
    job: str
    birth_date: datetime.date
    def __init__(self):
        self.first_name = field(default_factory=fake_ru.first_name)
        self.last_name = field(default_factory=fake_ru.last_name)
        self.age = field(default=random.randint(0, 100))
        self.job = field(default_factory=fake_ru.job)
        self.birth_date = field(default_factory=fake_ru.date_of_birth)