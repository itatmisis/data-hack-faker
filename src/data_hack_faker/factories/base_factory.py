from collections import OrderedDict

import factory


class BaseFactory(factory.Factory):
    id = factory.sequence(lambda n: n + 1)

    @staticmethod
    def configure_faker(field_name: str, settings: dict, locale: str) -> factory.Faker:
        return factory.Faker(
            settings[field_name]["provider"],
            **{
                k: OrderedDict(v) if isinstance(v, dict) else v
                for k, v in settings[field_name]["kwargs"].items()
            },
            locale=locale,
        )
