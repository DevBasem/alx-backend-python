#!/usr/bin/env python3
"""
Module to define a function with type annotations.
"""

from typing import Mapping, Any, TypeVar, Union

# Define a generic type variable for the return value
T = TypeVar('T')


def safely_get_value(
    dct: Mapping,
    key: Any,
    default: Union[T, None] = None
) -> Union[Any, T]:
    """
    Safely get a value from a dictionary.

    Args:
        dct (Mapping): The dictionary to search.
        key (Any): The key to look for.
        default (Union[T, None], optional): The default value if
        key is not found. Defaults to None.

    Returns:
        Union[Any, T]: The value associated with the key, or
        the default value if key is not found.
    """
    if key in dct:
        return dct[key]
    else:
        return default
