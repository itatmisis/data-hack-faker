from data_hack_faker.dataclasses.customer import Customer


def test_customer_generation():
    Customer(1, "Louis", "Silvester", 18, "89185553535")
