from factory import Faker

from . import BaseFactory
from ..dataclasses import Company


class CompanyFactory(BaseFactory):
    class Meta:
        model = Company

    name = Faker("company")
    location = Faker("administrative_unit")
    address = Faker("address")
    phone_number = Faker("bothify", text="8918#######")
