from dataclasses import fields

import pyspark.sql.dataframe

from .. import dataclasses as dhf_dc


def determine_dataclass_by_columns(
    df: pyspark.sql.dataframe.DataFrame,
) -> type[dhf_dc.BaseDataclass]:
    df_columns = df.columns
    dc_columns = {
        data: [field.name for field in fields(data)] for data in dhf_dc.available_dataclasses
    }
    for k, v in dc_columns.items():
        if df_columns == v:
            return k
    raise AttributeError("No suitable dataclass was found")
