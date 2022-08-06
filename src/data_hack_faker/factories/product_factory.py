import factory

from ..dataclasses import Product


class ProductFactory(factory.Factory):
    class Meta:
        model = Product

    id = factory.sequence(lambda n: n)
    name = factory.Faker("pystr", max_chars=10)
    price = factory.Faker("pyfloat", positive=True, left_digits=5, right_digits=2)
    date_produced = factory.Faker("date_time_this_decade")
    company_id = factory.Faker("pyint", min_value=0, max_value=9999)
