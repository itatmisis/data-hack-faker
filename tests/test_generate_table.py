from pathlib import Path

from data_hack_faker import factories
from data_hack_faker.sparktable import spark_inference


def test_generate_table():
    batch_size = 100
    for factory in [factories.CustomerFactory]:
        instances = factory.create_batch(size=batch_size)
        spark_inference.generate_table_from_list(
            instances, file_format="parquet", save_path=Path("../.tmp/")
        )
        spark_inference.generate_table_from_list(
            instances, file_format="orc", save_path=Path("../.tmp/")
        )
