from data_hack_faker.dataclasses import Customer
from data_hack_faker.factories import CustomerFactory
import pytest
from pytest_check import check


def check_customer(customer: Customer):
    with check:
        assert isinstance(customer.first_name, str)
        assert isinstance(customer.last_name, str)


def test_customer_factory():
    customer = CustomerFactory()
    check_customer(customer)


@pytest.mark.parametrize(
    "batch_size",
    [
        1,
        1_000,
        # 1_000_000
    ],
)
def test_customer_factory_benchmark(benchmark, batch_size):
    customers = benchmark(CustomerFactory.create_batch, size=batch_size)
    for customer in customers:
        check_customer(customer)
