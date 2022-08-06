from typing import Union

from .company_factory import CompanyFactory
from .customer_factory import CustomerFactory
from .employee_factory import EmployeeFactory
from .order_factory import OrderFactory
from .product_factory import ProductFactory

__all__ = [
    "CompanyFactory",
    "CustomerFactory",
    "EmployeeFactory",
    "OrderFactory",
    "ProductFactory",
]
types = Union[CompanyFactory, CustomerFactory, EmployeeFactory, OrderFactory, ProductFactory]
available_factories = [
    CompanyFactory,
    CustomerFactory,
    EmployeeFactory,
    OrderFactory,
    ProductFactory,
]
