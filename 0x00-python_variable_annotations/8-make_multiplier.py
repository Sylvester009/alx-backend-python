#!/usr/bin/env python3

"""type-annotated function make_multiplier
that takes a float multiplier as argument and returns a function
that multiplies a float by multiplier.
"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Function to create and return a function that multiplies a float
        by the specified multiplier.
    """
    def multiply(x: float) -> float:
        """multiplies a float by multiplier.
        """
        return x * multiplier
    return multiply
