from ..data_hack_faker.config import order_settings as settings
import factory

from . import BaseFactory
from ..dataclasses import Order

locale = settings["locale"] or "en_US"


class OrderFactory(BaseFactory):
    class Meta:
        model = Order

    # Default settings
    customer_id = factory.Faker("pyint", min_value=0, max_value=9999)
    product_id = factory.Faker("pyint", min_value=0, max_value=9999)
    date_produced = factory.Faker(
        "date_time_between", start_date="-30y", end_date="now", locale=locale
    )

    # Config settings
    if "id" in settings:
        id = BaseFactory.configure_faker("id", settings, locale)
    if "customer_id" in settings:
        customer_id = BaseFactory.configure_faker("customer_id", settings, locale)
    if "product_id" in settings:
        product_id = BaseFactory.configure_faker("product_id", settings, locale)
    if "date_produced" in settings:
        job = BaseFactory.configure_faker("date_produced", settings, locale)
