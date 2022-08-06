import factory

from ..dataclasses import Employee
from ..providers import JobProvider

factory.Faker.add_provider(JobProvider)


class EmployeeFactory(factory.Factory):
    class Meta:
        model = Employee

    id = factory.sequence(lambda n: n)
    first_name = factory.Faker("first_name")
    last_name = factory.Faker("last_name")
    age = factory.Faker("pyint", min_value=18, max_value=100)
    job = factory.Faker("JobProvider")
    company_id = factory.Faker("pyint", min_value=0, max_value=9999)
