#!/usr/bin/env python3
"""
This module provides a function to create a multiplier function.
"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Create a function that multiplies a float by a given multiplier.

    Args:
        multiplier (float): The multiplier to use.

    Returns:
        Callable[[float], float]: A function that multiplies a float by the multiplier.
    """
    def multiplier_func(x: float) -> float:
        """
        Multiply a float by the given multiplier.

        Args:
            x (float): The float to be multiplied.

        Returns:
            float: The result of the multiplication.
        """
        return x * multiplier

    return multiplier_func
