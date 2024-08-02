#!/usr/bin/env python3

"""type-annotated function (sum_list)
that takes a list (input_list) of floats as arguments
and returns their sum as a float.
"""


from typing import List


def sum_list(input_list: List[float]) -> float:
    """return the sum of a list of floats.
    """
    sum = 0.0

    for num in input_list:
        if isinstance(num, float):
            sum += num

    return sum
