from dataclasses import dataclass
from datetime import datetime

from pyspark.sql.types import (
    DoubleType,
    IntegerType,
    StringType,
    StructField,
    StructType,
    TimestampType,
)

from .base_dataclass import BaseDataclass


@dataclass(frozen=True)
class Product(BaseDataclass):
    name: str
    price: float
    date_produced: datetime
    company_id: int

    @staticmethod
    def schema() -> StructType:
        schema = StructType(
            [
                StructField("id", IntegerType(), False),
                StructField("name", StringType(), False),
                StructField("price", DoubleType(), False),
                StructField("date_produced", TimestampType(), False),
                StructField("company_id", IntegerType(), False),
            ]
        )
        return schema
