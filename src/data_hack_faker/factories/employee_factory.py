from ..config import employee_settings as settings
import factory

from . import BaseFactory
from ..dataclasses import Employee

locale = settings["locale"] or "en_US"


class EmployeeFactory(BaseFactory):
    class Meta:
        model = Employee

    # Default settings
    first_name = factory.Faker("first_name", locale=locale)
    last_name = factory.Faker("last_name", locale=locale)
    age = factory.Faker("pyint", min_value=18, max_value=65)
    job = factory.Faker("job", locale=locale)
    company_id = factory.sequence(lambda n: n + 1)

    # Config settings
    if "first_name" in settings:
        first_name = BaseFactory.configure_faker("first_name", settings, locale)
    if "last_name" in settings:
        last_name = BaseFactory.configure_faker("last_name", settings, locale)
    if "age" in settings:
        age = BaseFactory.configure_faker("age", settings, locale)
    if "job" in settings:
        job = BaseFactory.configure_faker("job", settings, locale)
    if "company_id" in settings:
        company_id = BaseFactory.configure_faker("company_id", settings, locale)
