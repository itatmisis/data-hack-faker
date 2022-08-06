import factory


class BaseFactory(factory.Factory):
    id = factory.sequence(lambda n: n + 1)
