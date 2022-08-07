from ..config import company_settings as settings
import factory

from . import BaseFactory
from ..dataclasses import Company

locale = settings["locale"] or "en_US"


class CompanyFactory(BaseFactory):
    class Meta:
        model = Company

    # Default settings
    name = factory.Faker("company", locale=locale)
    location = factory.Faker("administrative_unit", locale=locale)
    address = factory.Faker("city", locale=locale)
    phone_number = factory.Faker("bothify", text="8918#######")

    # Config settings
    if "name" in settings:
        name = BaseFactory.configure_faker("name", settings, locale)
    if "location" in settings:
        location = BaseFactory.configure_faker("location", settings, locale)
    if "address" in settings:
        address = BaseFactory.configure_faker("address", settings, locale)
    if "phone_number" in settings:
        phone_number = BaseFactory.configure_faker("phone_number", settings, locale)
