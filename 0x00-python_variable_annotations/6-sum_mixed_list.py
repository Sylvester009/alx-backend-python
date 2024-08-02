#!/usr/bin/env python3

"""type-annotated function (sum_mixed_list)
that takes a list (mxd_list) of integers and floats as arguments and
returns their sum as a float.
"""

from typing import List, Union


def sum_mixed_list(mxd_list: List[Union[int, float]]) -> float:
    """return the sum of a list of integers and floats.
    """
    max_sum = 0.0

    for idx in mxd_list:
        if isinstance(idx, int) or isinstance(idx, float):
            max_sum += idx

    return max_sum
