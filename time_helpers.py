"""time_helpers.py"""

from functools import partial
from itertools import accumulate, repeat, takewhile
from typing import Iterable

import pandas as pd
from toolz import pipe

td_0 = pd.Timedelta(0)
td_1D = pd.Timedelta("1D")


def gen_dates(
    start: str | pd.Timestamp,
    end: pd.Timestamp = pd.Timestamp.now(),
    step: pd.Timedelta = td_1D,
) -> Iterable[pd.Timestamp]:
    """Generate sorted list of days from start to end.

    Args:
        start (str | pd.Timestamp): Start date.
        end (pd.Timestamp, optional): End date. Defaults to pd.Timestamp.now().
        step (pd.Timedelta, optional): Distance between dates.
            Defaults to 1 day timedelta.

    Returns:
        list[pd.Timestamp]: List of sorted days.
    """
    dates = pipe(step, repeat, partial(accumulate, initial=pd.Timestamp(start)))
    return takewhile(lambda date: date < pd.Timestamp(end), dates)


def months_since(
    start: str | pd.Timestamp,
    end: str | pd.Timestamp | None = None,
) -> float:
    """Calculates number of months since start date.

    Args:
        start (str | pd.Timestamp): Start date.
        end (str| pd.Timestamp | None, optional): End date.
            Defaults to None, overwritten later to pd.Timestamp.now().

    Returns:
        float: Resulting number of months ellapsed until now.
    """
    if not end:
        end = pd.Timestamp.today()
    return (pd.Timestamp(end) - pd.Timestamp(start)).days / 365.25 * 12


def ts_to_date(ts: pd.Timestamp) -> pd.Timestamp:
    """Strips timestamp from clock time information.

    Args:
        ts (pd.Timestamp): Timestamp refering to the midnight of the day of
            the original timestamp.
    """
    return ts.replace(hour=0, minute=0, second=0, microsecond=0)
