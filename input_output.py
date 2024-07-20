"""common/input_output.py"""

from pathlib import Path
import tomllib

import numpy as np
import numexpr


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


def read_toml_file(filename: Path) -> dict:
    """Reads TOML file using tomllib and returns a dict.

    Args:
        filename (Path): Path object to the TOML file to be loaded.

    Returns:
        dict: Dict containing the loaded data.
    """
    with filename.open("rb") as toml_file:
        return tomllib.load(toml_file)
