from factory import Faker
from config import employee_settings as settings
from . import BaseFactory
from ..dataclasses import Employee

Faker.override_default_locale('ru_RU')


class EmployeeFactory(BaseFactory):
    class Meta:
        model = Employee

    first_name = Faker("first_name")
    last_name = Faker("last_name")
    age = Faker("pyint", min_value=settings['min'], max_value=settings['max'])
    job = Faker("job")
    company_id = Faker("pyint", min_value=0, max_value=9999)
