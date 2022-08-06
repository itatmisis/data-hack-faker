from data_hack_faker.factories import CustomerFactory
from src.data_hack_faker.sparktable import spark_inference


def test_generate_table():
    batch_size = 1_000
    customers = CustomerFactory.create_batch(size=batch_size)
    spark_inference.generate_table_from_list(customers)
