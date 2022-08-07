import factory

from . import BaseFactory
from ..config_parser import customer_settings as settings
from ..dataclasses import Customer

locale = settings["locale"] or "en_US"


class CustomerFactory(BaseFactory):
    class Meta:
        model = Customer

    # Default settings
    first_name = factory.Faker("first_name", locale=locale)
    last_name = factory.Faker("last_name", locale=locale)
    age = factory.Faker("pyint", min_value=18, max_value=35)
    phone_number = factory.Faker("bothify", text="8918#######")

    # Config settings
    if "first_name" in settings:
        first_name = BaseFactory.configure_faker("first_name", settings, locale)
    if "last_name" in settings:
        last_name = BaseFactory.configure_faker("last_name", settings, locale)
    if "age" in settings:
        age = BaseFactory.configure_faker("age", settings, locale)
    if "phone_number" in settings:
        phone_number = BaseFactory.configure_faker("phone_number", settings, locale)
