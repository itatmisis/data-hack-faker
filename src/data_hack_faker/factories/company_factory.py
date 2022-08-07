from factory import Faker
from config import company_settings as settings
from . import BaseFactory
from ..dataclasses import Company

Faker.override_default_locale('ru_RU')


class CompanyFactory(BaseFactory):
    class Meta:
        model = Company

    name = Faker("company")
    location = Faker("administrative_unit")
    address = Faker("address")
    phone_number = Faker("bothify", text=settings['phone']['mask'])
