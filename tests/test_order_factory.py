from datetime import datetime

from data_hack_faker.dataclasses import Order
from data_hack_faker.factories import OrderFactory
import pytest
from pytest_check import check


def check_order(order: Order):
    with check:
        assert isinstance(order.product_id, int)
        assert isinstance(order.customer_id, int)
        assert isinstance(order.created_at, datetime)


def test_order_factory():
    order = OrderFactory()
    check_order(order)


@pytest.mark.parametrize(
    "batch_size",
    [
        1,
        1_000,
        # 1_000_000
    ],
)
def test_order_factory_benchmark(benchmark, batch_size):
    orders = benchmark(OrderFactory.create_batch, size=batch_size)
    for order in orders:
        check_order(order)
