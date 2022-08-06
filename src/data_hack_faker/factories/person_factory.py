import factory

from ..dataclasses import Customer
from ..providers import JobProvider

factory.Faker.add_provider(JobProvider)


class PersonFactory(factory.Factory):
    class Meta:
        model = Customer

    first_name = factory.Faker("first_name")
    last_name = factory.Faker("last_name")
    age = factory.Faker("pyint", min_value=18, max_value=100)
    phone_number = factory.Faker("bothify", text="8918#######")
