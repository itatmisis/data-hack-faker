from data_hack_faker.dataclasses import Company
from data_hack_faker.factories import CompanyFactory
import pytest
from pytest_check import check


def check_company(company: Company):
    with check:
        assert isinstance(company.name, str)
        assert isinstance(company.address, str)
        assert isinstance(company.location, str)


def test_company_factory():
    company = CompanyFactory()
    print(company)
    check_company(company)


@pytest.mark.parametrize(
    "batch_size",
    [
        1,
        1_000,
        # 1_000_000
    ],
)
def test_company_factory_benchmark(benchmark, batch_size):
    companies = benchmark(CompanyFactory.create_batch, size=batch_size)
    for company in companies:
        check_company(company)
