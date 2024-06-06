#!/usr/bin/env python3
"""
This module provides a function to convert a string and
an int or float to a tuple.
"""

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Convert a string and an int or float to a tuple.

    Args:
        k (str): The string key.
        v (Union[int, float]): The integer or float value.

    Returns:
        Tuple[str, float]: The tuple containing the string key
        and the square of the value.
    """
    return k, v ** 2.0
