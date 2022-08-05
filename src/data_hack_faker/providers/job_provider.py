from collections import OrderedDict

from faker.providers import BaseProvider


# create new provider class
class JobProvider(BaseProvider):
    jobs = OrderedDict({"Программист": 0.15, "Сантехник": 0.5, "Слесарь": 0.35})

    def custom_job(self) -> str:
        return self.random_element(self.jobs)
