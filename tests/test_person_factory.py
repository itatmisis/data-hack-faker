from data_hack_faker.dataclasses import Person
from data_hack_faker.factories import PersonFactory
import pytest
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


@pytest.mark.parametrize(
    "batch_size",
    [
        1,
        1_000,
        # 1_000_000
    ],
)
def test_person_factory_benchmark(benchmark, batch_size):
    persons = benchmark(PersonFactory.create_batch, size=batch_size)
    for person in persons:
        check_person(person)
