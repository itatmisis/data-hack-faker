from dataclasses import dataclass

from pyspark.sql.types import IntegerType, StringType, StructField, StructType

from .base_dataclass import BaseDataclass


@dataclass(frozen=True)
class Employee(BaseDataclass):
    first_name: str
    last_name: str
    age: int
    job: str
    company_id: int

    @staticmethod
    def schema() -> StructType:
        schema = StructType(
            [
                StructField("id", IntegerType(), False),
                StructField("first_name", StringType(), False),
                StructField("last_name", StringType(), False),
                StructField("age", IntegerType(), False),
                StructField("job", StringType(), False),
                StructField("company_id", IntegerType(), False),
            ]
        )
        return schema
