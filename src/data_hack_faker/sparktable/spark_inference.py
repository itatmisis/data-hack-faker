from __future__ import annotations

from dataclasses import astuple, fields
import os
from pathlib import Path

from pyspark.sql import SparkSession

from ..dataclasses import Company, Customer, Employee, Order, Product

APP_NAME = "data-hack-faker"
spark_builder = SparkSession.builder.appName(APP_NAME).getOrCreate()


def prepare_data_list(
    data_list: list[Company | Customer | Employee | Order | Product],
) -> list[tuple]:
    new_data_list = list(map(astuple, data_list))
    return new_data_list


def generate_table_from_list(
    data_list: list[Company | Customer | Employee | Order | Product],
    file_format: str,
    save_path: os.PathLike = Path(".tmp/"),  # noqa: B008
):
    data_class_name = data_list[0].__class__.__name__
    columns = [field.name for field in fields(data_list[0])]
    prepared_data_list = prepare_data_list(data_list)
    df = spark_builder.createDataFrame(prepared_data_list).toDF(*columns)
    file_path = (Path(save_path) / Path(f"{data_class_name}.{file_format}")).__str__()
    (df.write.mode("overwrite").format(file_format).save(file_path))


def load_table_from_filepath(
    file_path: os.PathLike,
):
    df = spark_builder.read.load(file_path.__str__())
    return df
