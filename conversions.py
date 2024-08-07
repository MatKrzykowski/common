"conversions.py"

import datetime as dt
import pandas as pd


def str_to_datetime(time_str: str) -> dt.datetime:
    """Converts string to datetime object using pandas."""
    return pd.to_datetime(time_str).to_pydatetime()
