from dataclasses import dataclass
from datetime import datetime

from .base_dataclass import BaseDataclass


@dataclass(frozen=True)
class Order(BaseDataclass):
    person_id: str
    product_id: int
    created_at: datetime
