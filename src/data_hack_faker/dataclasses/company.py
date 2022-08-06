from dataclasses import dataclass

from pyspark.sql.types import IntegerType, StringType, StructField, StructType

from .base_dataclass import BaseDataclass


@dataclass(frozen=True)
class Company(BaseDataclass):
    name: str
    location: str
    address: str
    phone_number: str

    @staticmethod
    def schema() -> StructType:
        schema = StructType(
            [
                StructField("id", IntegerType(), False),
                StructField("name", StringType(), False),
                StructField("location", StringType(), False),
                StructField("address", StringType(), False),
                StructField("phone_number", StringType(), False),
            ]
        )
        return schema
