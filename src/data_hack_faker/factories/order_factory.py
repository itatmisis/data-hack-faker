import factory

from . import BaseFactory
from ..dataclasses import Order


class OrderFactory(BaseFactory):
    class Meta:
        model = Order

    id = factory.sequence(lambda n: n)
    customer_id = factory.Faker("pyint", min_value=0, max_value=9999)
    product_id = factory.Faker("pyint", min_value=0, max_value=9999)
    date_produced = factory.Faker("date_time_between", start_date="-30y", end_date="now")
