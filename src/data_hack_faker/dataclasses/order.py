from dataclasses import dataclass
from datetime import datetime

from pyspark.sql.types import IntegerType, StructField, StructType, TimestampType

from .base_dataclass import BaseDataclass


@dataclass(frozen=True)
class Order(BaseDataclass):
    customer_id: int
    product_id: int
    date_produced: datetime

    @staticmethod
    def schema() -> StructType:
        schema = StructType(
            [
                StructField("id", IntegerType(), False),
                StructField("customer_id", IntegerType(), False),
                StructField("product_id", IntegerType(), False),
                StructField("date_produced", TimestampType(), False),
            ]
        )
        return schema
