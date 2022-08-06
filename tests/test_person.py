from src.data_hack_faker.dataclasses.customer import Customer


def test_person_generation():
    Customer("Louis", "Silvester", 18, "89185553535")
