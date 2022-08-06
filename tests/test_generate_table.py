from pathlib import Path

from data_hack_faker import factories
from data_hack_faker.sparktable import spark_inference
import pandas as pd


def test_generate_table():
    batch_size = 1_000
    for factory in [factories.CustomerFactory]:
        instances = factory.create_batch(size=batch_size)
        class_name: str = instances[0].__class__.__name__
        file_formats = ["parquet"]
        for file_format in file_formats:
            df_in_memory = spark_inference.generate_table_from_list(
                instances, file_format=file_format, save_path=Path("../.tmp/")
            )
            df_from_file = spark_inference.load_table_from_filepath(
                Path(f"../.tmp/{class_name.lower()}_{file_format}")
            )
            pd.testing.assert_frame_equal(
                df_in_memory.sort_values(by="id").set_index("id"),
                df_from_file.sort_values(by="id").set_index("id"),
            )


def test_benchmark_generate_table(benchmark):
    benchmark(test_generate_table)
