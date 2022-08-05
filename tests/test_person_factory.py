from data_hack_faker.factories import PersonFactory


def test_person_factory():
    person = PersonFactory()
    assert isinstance(person.first_name, str)
    assert isinstance(person.last_name, str)
    assert 18 < person.age < 100
    assert len(person.phone_number) == 11
    assert person.phone_number[:4] == "8918"
    return person
