from data_hack_faker.providers import JobProvider
import faker


def test_job_provider():
    fake = faker.Faker()
    fake.add_provider(JobProvider)
    jobs = []
    for i in range(len(JobProvider.jobs)):
        jobs.append(fake.unique.custom_job())
    for job in jobs:
        assert job in JobProvider.jobs
    return jobs
