"conversions.py"

import datetime as dt

import numexpr
import pandas as pd


def str_to_datetime(time_str: str) -> dt.datetime:
    """Converts string to datetime object using pandas."""
    return pd.to_datetime(time_str).to_pydatetime()


def expr_to_float(x: str | float) -> float:
    """Converts a simple expression (even simply a number) into a number.

    Args:
        x (str | float): A string expression or a number.

    Returns:
        float: Result of the expression.
    """
    match x:
        case float():
            return x
        case str():
            return float(+numexpr.evaluate(x))
    return float(x)


def td_to_days(td: dt.timedelta) -> float:
    """Converts timedelta object to days.

    Args:
        td (dt.timedelta): Timedelta object.

    Returns:
        float: Number of days representing td. 
    """
    return td.total_seconds() / 60 / 60 / 24
