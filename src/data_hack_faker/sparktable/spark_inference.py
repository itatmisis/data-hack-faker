from __future__ import annotations

from dataclasses import astuple, fields
import os
from pathlib import Path

from pyspark.sql import SparkSession
import pyspark.sql.dataframe

from . import utils
from .. import dataclasses as dhf_dc

APP_NAME = "data-hack-faker"
spark_builder = SparkSession.builder.appName(APP_NAME).getOrCreate()


def prepare_data_list(
    data_list: list[dhf_dc.types],
) -> list[tuple]:
    new_data_list = list(map(astuple, data_list))
    return new_data_list


def generate_table_from_list(
    data_list: list[dhf_dc.types],
) -> pyspark.sql.dataframe.DataFrame:
    columns = [field.name for field in fields(data_list[0])]
    schema = data_list[0].schema()
    prepared_data_list = prepare_data_list(data_list)
    df = spark_builder.createDataFrame(prepared_data_list, schema=schema).toDF(*columns)
    return df


def save_table(
    df: pyspark.sql.dataframe.DataFrame,
    file_format: str,
    save_path: os.PathLike,
):
    data_class = utils.determine_dataclass_by_columns(df)
    data_class_name = data_class.__name__.lower()

    file_path = (Path(save_path) / Path(f"{data_class_name}_{file_format}")).__str__()
    df.write.mode("overwrite").format(file_format).options(header="True").save(file_path)


def load_table_from_filepath(
    file_path: os.PathLike,
    file_format: str = "parquet",
) -> pyspark.sql.dataframe.DataFrame:
    first_df = spark_builder.read.options(header="True", inferSchema="True").load(
        file_path.__str__(), format=file_format
    )
    data_class = utils.determine_dataclass_by_columns(first_df)
    df = spark_builder.read.options(header="True").load(
        file_path.__str__(), format=file_format, schema=data_class.schema()
    )
    return df
