import factory

from ..dataclasses import Company


class CompanyFactory(factory.Factory):
    class Meta:
        model = Company

    id = factory.sequence(lambda n: n)
    name = factory.Faker("company")
    location = factory.Faker("administrative_unit")
    address = factory.Faker("address")
    phone_number = factory.Faker("bothify", text="8918#######")
