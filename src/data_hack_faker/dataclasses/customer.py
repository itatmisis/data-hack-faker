from dataclasses import dataclass
from .base_dataclass import BaseDataclass


@dataclass(frozen=True)
class Customer(BaseDataclass):
    first_name: str
    last_name: str
    age: int
    phone_number: str
