from dataclasses import dataclass
from datetime import date

from .base_dataclass import BaseDataclass


@dataclass(frozen=True)
class Product(BaseDataclass):
    name: str
    price: float
    date_produced: date
    company_id: int
