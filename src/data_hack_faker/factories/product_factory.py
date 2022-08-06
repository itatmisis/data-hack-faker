from factory import Faker

from . import BaseFactory
from ..dataclasses import Product


class ProductFactory(BaseFactory):
    class Meta:
        model = Product

    name = Faker("pystr", max_chars=10)
    price = Faker("pyfloat", positive=True, left_digits=5, right_digits=2)
    date_produced = Faker("date_time_this_decade")
    company_id = Faker("pyint", min_value=0, max_value=9999)
