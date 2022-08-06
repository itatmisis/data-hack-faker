from factory import Faker

from . import BaseFactory
from ..dataclasses import Customer


class CustomerFactory(BaseFactory):
    class Meta:
        model = Customer

    first_name = Faker("first_name")
    last_name = Faker("last_name")
    age = Faker("pyint", min_value=18, max_value=100)
    phone_number = Faker("bothify", text="8918#######")
