import factory

from . import BaseFactory
from ..dataclasses import Employee


class EmployeeFactory(BaseFactory):
    class Meta:
        model = Employee

    first_name = factory.Faker("first_name")
    last_name = factory.Faker("last_name")
    age = factory.Faker("pyint", min_value=18, max_value=100)
    job = factory.Faker("job")
    company_id = factory.Faker("pyint", min_value=0, max_value=9999)
