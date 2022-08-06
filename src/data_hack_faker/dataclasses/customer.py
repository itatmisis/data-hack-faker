from dataclasses import dataclass


@dataclass(frozen=True)
class Person:
    first_name: str
    last_name: str
    age: int
    phone_number: str
