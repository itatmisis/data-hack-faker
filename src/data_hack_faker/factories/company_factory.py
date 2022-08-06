import factory

from . import BaseFactory
from ..dataclasses import Company


class CompanyFactory(BaseFactory):
    class Meta:
        model = Company

    id = factory.sequence(lambda n: n)
    name = factory.Faker("company")
    location = factory.Faker("administrative_unit")
    address = factory.Faker("city")
    phone_number = factory.Faker("bothify", text="8918#######")
