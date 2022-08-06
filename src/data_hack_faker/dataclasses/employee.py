from dataclasses import dataclass

from .base_dataclass import BaseDataclass


@dataclass(frozen=True)
class Employee(BaseDataclass):
    first_name: str
    last_name: str
    age: int
    job: str
    company_id: int
