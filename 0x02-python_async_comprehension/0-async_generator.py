#!/usr/bin/env python3

"""
a coroutine called async_generator
that takes no arguments. It loops
10 times and each time, it
asynchronously wait 1 second
and then yield a random number
between 0 and 10.
"""

import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, none, none]:
    """loops 10 times and each time,
    it asynchronously wait 1 second and
    then yield a random number between 0 and 10.
    """

    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
