from dataclasses import fields

import pyspark.sql.dataframe

from .. import dataclasses as dhf_dc


def determine_dataclass_by_columns(
    df: pyspark.sql.dataframe.DataFrame,
):
    df_columns = df.columns
    dc_columns = {
        data: [field.name for field in fields(data)] for data in dhf_dc.available_dataclasses
    }
    for k, v in dc_columns.items():
        if df_columns == v:
            return k
    raise AttributeError("No suitable dataclass was found")


def construct_data_list_from_df(
    df: pyspark.sql.dataframe.DataFrame,
):
    data_class = determine_dataclass_by_columns(df)
    data_list = [data_class(**x.asDict()) for x in df.collect()]
    return data_list
