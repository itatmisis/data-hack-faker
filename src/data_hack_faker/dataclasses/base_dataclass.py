from dataclasses import dataclass

from pyspark.sql.types import IntegerType, StructField, StructType


@dataclass(frozen=True)
class BaseDataclass:
    id: int

    @staticmethod
    def schema() -> StructType:
        schema = StructType([StructField("id", IntegerType(), False)])
        return schema
