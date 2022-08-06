from datetime import date

from data_hack_faker.dataclasses import Product
from data_hack_faker.factories import ProductFactory
import pytest
from pytest_check import check


def check_product(product: Product):
    with check:
        assert isinstance(product.name, str)
        assert isinstance(product.price, float)
        assert isinstance(product.date_produced, date)
        assert isinstance(product.company_id, int)


def test_product_factory():
    product = ProductFactory()
    check_product(product)


@pytest.mark.parametrize(
    "batch_size",
    [
        1,
        1_000,
        # 1_000_000
    ],
)
def test_product_factory_benchmark(benchmark, batch_size):
    products = benchmark(ProductFactory.create_batch, size=batch_size)
    for product in products:
        check_product(product)
