from config import company_settings as settings
from factory import Faker

from . import BaseFactory
from ..dataclasses import Company

Faker.override_default_locale(settings["locale"] or "ru_RU")


class CompanyFactory(BaseFactory):
    class Meta:
        model = Company

    if "name" in settings:
        name = Faker(settings["name"]["provider"], **settings["name"]["kwargs"])
    else:
        name = Faker("company")
    location = Faker("administrative_unit")
    address = Faker("address")
    if "phone_number" in settings:
        phone_number = Faker(
            settings["phone_number"]["provider'"], **settings["phone_number"]["kwargs"]
        )
    else:
        phone_number = Faker("bothify", text="8918#######")
