from dataclasses import dataclass

from pyspark.sql.types import StructType


@dataclass(frozen=True)
class BaseDataclass:
    id: int

    @staticmethod
    def schema() -> StructType:
        schema = StructType()
        return schema
