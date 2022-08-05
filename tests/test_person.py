from data_hack_faker.dataclasses.person import Person


def test_person_generation():
    person = Person("Louis", "Silverster", 18, "89185553535")
    return person
