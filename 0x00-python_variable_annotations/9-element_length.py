#!/usr/bin/env python3

"""annotate the below function's parameters
    and return values with the appropriate types
"""


from typing import Iterable, List, Tuple, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """returns a list of tuples with the string
        and its length.
    """
    return [(i, len(i)) for i in lst]
