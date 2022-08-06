from dataclasses import dataclass


@dataclass(frozen=True)
class Employee:
    first_name: str
    last_name: str
    age: int
    job: str
    company_id: int
