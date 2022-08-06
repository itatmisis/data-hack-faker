from pathlib import Path

from data_hack_faker import factories
from data_hack_faker.sparktable import spark_inference
import pandas as pd


def test_generate_table():
    batch_size = 100
    for factory in [factories.CustomerFactory]:
        instances = factory.create_batch(size=batch_size)
        class_name = instances[0].__class__.__name__
        file_formats = ["parquet", "orc"]
        for file_format in file_formats:
            df_in_memory = spark_inference.generate_table_from_list(
                instances, file_format=file_format, save_path=Path("../.tmp/")
            )
            df_from_file = spark_inference.load_table_from_filepath(
                Path(f"../.tmp/{class_name}_{file_format}")
            )
            pd.testing.assert_frame_equal(df_in_memory, df_from_file)
