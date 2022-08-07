from data_hack_faker.dataclasses import Employee
from data_hack_faker.factories import EmployeeFactory
import pytest
from pytest_check import check


def check_employee(employee: Employee):
    with check:
        assert isinstance(employee.first_name, str)
        assert isinstance(employee.last_name, str)
        assert isinstance(employee.job, str)
        assert isinstance(employee.company_id, int)
        assert employee.company_id > 0


def test_employee_factory():
    employee = EmployeeFactory()
    check_employee(employee)


@pytest.mark.parametrize(
    "batch_size",
    [
        1,
        1_000,
        # 1_000_000
    ],
)
def test_employee_factory_benchmark(benchmark, batch_size):
    employees = benchmark(EmployeeFactory.create_batch, size=batch_size)
    for employee in employees:
        check_employee(employee)
