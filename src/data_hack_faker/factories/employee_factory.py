from factory import Faker

from . import BaseFactory
from ..dataclasses import Employee


class EmployeeFactory(BaseFactory):
    class Meta:
        model = Employee

    first_name = Faker("first_name")
    last_name = Faker("last_name")
    age = Faker("pyint", min_value=18, max_value=100)
    job = Faker("job")
    company_id = Faker("pyint", min_value=0, max_value=9999)
