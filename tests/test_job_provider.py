import faker
from pytest_check import check
from src.data_hack_faker.providers import JobProvider


def test_job_provider():
    fake = faker.Faker()
    fake.add_provider(JobProvider)
    jobs = []
    for _ in JobProvider.jobs:
        jobs.append(fake.unique.custom_job())
    for job in jobs:
        with check:
            assert job in JobProvider.jobs
    return jobs
