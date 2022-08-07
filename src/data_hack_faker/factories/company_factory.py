from collections import OrderedDict

from config import company_settings as settings
from factory import Faker

from . import BaseFactory
from ..dataclasses import Company

Faker.override_default_locale(settings["locale"] or "ru_RU")


class CompanyFactory(BaseFactory):
    class Meta:
        model = Company

    if "name" in settings:
        name = Faker(
            settings["name"]["provider"],
            **{
                k: OrderedDict(v) if isinstance(v, dict) else v
                for k, v in settings["name"]["kwargs"].items()
            },
        )
    else:
        name = Faker("company")
    location = Faker("administrative_unit")
    address = Faker("address")
    if "phone_number" in settings:
        phone_number = Faker(
            settings["phone_number"]["provider'"],
            **{
                k: OrderedDict(v) if isinstance(v, dict) else v
                for k, v in settings["name"]["kwargs"].items()
            },
        )
    else:
        phone_number = Faker("bothify", text="8918#######")
