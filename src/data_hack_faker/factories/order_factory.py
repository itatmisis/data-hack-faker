from config import order_settings as settings
from factory import Faker

from . import BaseFactory
from ..dataclasses import Order

Faker.override_default_locale(settings["locale"] or "ru_RU")


class OrderFactory(BaseFactory):
    class Meta:
        model = Order

    customer_id = Faker("pyint", min_value=0, max_value=9999)
    product_id = Faker("pyint", min_value=0, max_value=9999)
    created_at = Faker("date_time_this_month")
