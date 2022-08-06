from dataclasses import dataclass
from .base_dataclass import BaseDataclass

@dataclass(frozen=True)
class Company(BaseDataclass):
    name: str
    location: str
    address: str
    phone_number: str
