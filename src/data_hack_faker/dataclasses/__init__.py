from __future__ import annotations

from typing import Type, Union

from .base_dataclass import BaseDataclass
from .company import Company
from .customer import Customer
from .employee import Employee
from .order import Order
from .product import Product

__all__ = ["Company", "Customer", "Employee", "Order", "Product"]
types = Type[Union[Company, Customer, Employee, Order, Product]]
available_dataclasses = [
    Company,
    Customer,
    Employee,
    Order,
    Product,
]  # type: list[Type[BaseDataclass]]
