from factory import Faker

from . import BaseFactory
from ..dataclasses import Customer
from config import customer_settings as settings

Faker.override_default_locale('ru_RU')

class CustomerFactory(BaseFactory):
    class Meta:
        model = Customer

    first_name = Faker("first_name")
    last_name = Faker("last_name")
    age = Faker("pyint", min_value=settings['age']['min'], max_value=settings['age']['max'])
    phone_number = Faker("bothify", text=settings['phone_number']['mask'])
