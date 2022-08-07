from pathlib import Path

from data_hack_faker import factories
from data_hack_faker.sparktable import spark_inference
from pyspark_test import assert_pyspark_df_equal
import pytest


@pytest.mark.parametrize("batch_size", [100])
@pytest.mark.parametrize("file_format", ["parquet", "csv"])
@pytest.mark.parametrize("factory", factories.available_factories)
def test_generate_table(batch_size, file_format, factory):
    save_path = Path("../.tmp")
    instances = factory.create_batch(size=batch_size)
    class_name: str = factory._meta.model.__name__.lower()
    file_path = save_path / Path(f"{class_name}_{file_format}")
    df_in_memory = spark_inference.generate_table_from_list(instances)
    spark_inference.save_table(df_in_memory, file_format=file_format, save_path=save_path)
    df_from_file = spark_inference.load_table_from_filepath(file_path, file_format)
    assert_pyspark_df_equal(df_in_memory.sort("id"), df_from_file.sort("id"))


@pytest.mark.parametrize("factory", [factories.CompanyFactory])
def test_benchmark_generate_table(benchmark, factory):
    benchmark(test_generate_table, 1_000, "parquet", factory)
