from config import product_settings as settings
import factory
from factory import Faker

from . import BaseFactory
from ..dataclasses import Product

Faker.override_default_locale(settings["locale"] or "ru_RU")


class ProductFactory(BaseFactory):
    class Meta:
        model = Product

    id = factory.sequence(lambda n: n)
    name = factory.Faker("pystr", min_chars=None, max_chars=20)
    price = factory.Faker("pyfloat", positive=True, left_digits=5, right_digits=2)
    date_produced = factory.Faker("date_time_between", start_date="-30y", end_date="now")
    company_id = factory.Faker("pyint", min_value=0, max_value=9999)
