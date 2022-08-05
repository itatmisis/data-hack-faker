from data_hack_faker.dataclasses import Person
from data_hack_faker.factories import PersonFactory
from pytest_check import check


def check_person(person: Person):
    with check:
        assert isinstance(person.first_name, str)
        assert isinstance(person.last_name, str)
        assert 18 <= person.age <= 100
        assert len(person.phone_number) == 11
        assert person.phone_number[:4] == "8918"


def test_person_factory():
    person = PersonFactory()
    check_person(person)


def test_person_factory_benchmark(benchmark):
    persons = benchmark(PersonFactory.create_batch, size=10_000)
    for person in persons:
        with check:
            check_person(person)
