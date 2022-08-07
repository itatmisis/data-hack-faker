from config import product_settings as settings
import factory

from . import BaseFactory
from ..dataclasses import Product

locale = settings["locale"] or "en_US"


class ProductFactory(BaseFactory):
    class Meta:
        model = Product

    # Default settings
    id = factory.sequence(lambda n: n)
    name = factory.Faker("pystr", min_chars=None, max_chars=20)
    price = factory.Faker("pyfloat", positive=True, left_digits=5, right_digits=2)
    date_produced = factory.Faker(
        "date_time_between", start_date="-30y", end_date="now", locale=locale
    )
    company_id = factory.Faker("pyint", min_value=0, max_value=9999)

    # Config settings
    if "id" in settings:
        id = BaseFactory.configure_faker("id", settings, locale)
    if "name" in settings:
        name = BaseFactory.configure_faker("name", settings, locale)
    if "price" in settings:
        price = BaseFactory.configure_faker("price", settings, locale)
    if "date_produced" in settings:
        date_produced = BaseFactory.configure_faker("date_produced", settings, locale)
    if "company_id" in settings:
        company_id = BaseFactory.configure_faker("company_id", settings, locale)
