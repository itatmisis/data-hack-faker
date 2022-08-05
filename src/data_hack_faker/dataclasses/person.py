from dataclasses import dataclass


@dataclass
class Person:
    first_name: str
    last_name: str
    age: int
    phone_number: str
