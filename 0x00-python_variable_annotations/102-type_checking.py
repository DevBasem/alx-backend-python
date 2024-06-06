#!/usr/bin/env python3
"""
Module to define a function with type annotations.
"""

from typing import Tuple, List


def zoom_array(lst: Tuple[int, ...], factor: int = 2) -> List[int]:
    """
    Zoom in on the elements of a tuple by repeating each element.

    Args:
        lst (Tuple[int, ...]): The input tuple of integers.
        factor (int, optional): The factor by which to zoom in.
        Defaults to 2.

    Returns:
        List[int]: A list containing each element of the input tuple
        repeated by the specified factor.
    """
    zoomed_in = []  # Initialize an empty list
    for item in lst:
        zoomed_in.extend([item] * factor)
    return zoomed_in


if __name__ == "__main__":
    array = (12, 72, 91)

    zoom_2x = zoom_array(array)

    zoom_3x = zoom_array(array, 3)
