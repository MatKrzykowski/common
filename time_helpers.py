"""time_helpers.py"""

from itertools import accumulate, repeat, takewhile
from typing import Iterable
import pandas as pd

td_0 = pd.Timedelta(0)


def gen_dates(
    start: str | pd.Timestamp,
    end: pd.Timestamp = pd.Timestamp.now(),
    step: int = 1
) -> Iterable[pd.Timestamp]:
    """Generate sorted list of days from start to end.

    Args:
        start (str | pd.Timestamp): Start date.
        end (pd.Timestamp, optional): End date. Defaults to pd.Timestamp.now().
        step (int, optional): Distance between days. Defaults to 1.

    Returns:
        list[pd.Timestamp]: List of sorted days.
    """
    return takewhile(
        lambda date: date < end,
        accumulate(
            repeat(
                pd.Timedelta(days=step)
            ),
            initial=pd.Timestamp(start)
        )
    )
