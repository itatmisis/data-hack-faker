from dataclasses import dataclass, field
import datetime
import random

from faker import Faker

fake_ru = Faker(locale="ru_RU")


@dataclass
class Person:
    first_name: str = field(default_factory=fake_ru.first_name)
    last_name: str = field(default_factory=fake_ru.last_name)
    age: int = field(default=random.randint(0, 100))
    job: str = field(default_factory=fake_ru.job)
