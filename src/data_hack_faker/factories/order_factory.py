import factory

from ..dataclasses import Order


class OrderFactory(factory.Factory):
    class Meta:
        model = Order

    id = factory.sequence(lambda n: n)
    customer_id = factory.Faker("pyint", min_value=0, max_value=9999)
    product_id = factory.Faker("pyint", min_value=0, max_value=9999)
    created_at = factory.Faker("date_time_between", start_date="-30y", end_date="now")
