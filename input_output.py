"""common/input_output.py"""

import os
from pathlib import Path
import shutil
import tomllib
from typing import Callable

import numpy as np
import pandas as pd
import termcolor

from common.time_helpers import td_0


def pretty_float(x: float, max_digits: int = 5) -> str:
    """Returns "pretty" string given a number, without trailing 0s.

    Args:
        x (float): Number to be represented as string.
        max_digits (int, optional): Max number of significant digits.
            Defaults to 5.

    Returns:
        str: "Pretty" representation of an input number.
    """
    n_digits_whole_part = max(int(np.log10(x)), 0)
    digits = max(max_digits - n_digits_whole_part, 0)
    return f"{x:.{digits}f}"


def print_timedelta(td: pd.Timedelta) -> None:
    """Prints timedelta with color.

    Args:
        td (pd.Timedelta): Timedelta object.
    """
    if td > td_0:
        print(termcolor.colored("Remaining:", "red"), td)
    else:
        print(termcolor.colored("Ahead:", "green"), -td)


def read_toml_file(filename: Path) -> dict:
    """Reads TOML file using tomllib and returns a dict.

    Args:
        filename (Path): Path object to the TOML file to be loaded.

    Returns:
        dict: Dict containing the loaded data.
    """
    with filename.open("rb") as toml_file:
        return tomllib.load(toml_file)


def terminal_width() -> int:
    return shutil.get_terminal_size().columns


def line(symbol: str = "=", width: int = 80) -> str:
    """Returns string of given symbol and width"""
    return symbol * width


def print_heading(title: str, width: int = None, symbol: str = "#") -> None:
    if not width:
        width = terminal_width()
    print("\n".join([
        line(symbol, width),
        f"{symbol}{title:^{width-2}}{symbol}",
        line(symbol, width),
    ]))


def is_windows() -> bool:
    """Check if script is running on Windows or Unix"""
    return os.name == 'nt'


def clear_screen() -> None:
    """Clears terminal screen"""
    if is_windows():
        os.system("cls")
    else:
        os.system("clear")


def find_filepath(cond: Callable, dir_path: Path | str = ".") -> str:
    """Find filepath given condition and optional directory path.

    Args:
        cond (Callable): Filter used to find specified file.
        dir_path (Path | str, optional): Directory path. Defaults to ".".

    Returns:
        str: Name of the file.
    """
    files = list(
        filter(
            cond,
            os.listdir(dir_path)
        )
    )
    if len(files) != 1:
        assert False
    return files[0]

def move_file_if_exists(source, dest) -> None:
    if os.path.isfile(
        os.path.expanduser(source)
    ):
        shutil.move(
            os.path.expanduser(source),
            dest
        )
        print("File moved")
    else:
        print("File does not exist")
