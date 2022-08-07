from dataclasses import dataclass

from pyspark.sql.types import IntegerType, StringType, StructField, StructType

from .base_dataclass import BaseDataclass


@dataclass(frozen=True)
class Customer(BaseDataclass):
    first_name: str
    last_name: str
    age: int
    phone_number: str

    @staticmethod
    def schema() -> StructType:
        schema = StructType(
            [
                StructField("id", IntegerType(), False),
                StructField("first_name", StringType(), False),
                StructField("last_name", StringType(), False),
                StructField("age", IntegerType(), False),
                StructField("phone_number", StringType(), False),
            ]
        )
        return schema
