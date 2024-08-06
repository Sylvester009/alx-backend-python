#!/usr/bin/env python3

"""
A 'measure_runtime' coroutine that will execute
async_comprehension four times in parallel
using asyncio.gather.
measure_runtime should measure the total
runtime and return it.
"""

import asyncio
from random import uniform
from typing import Generator, List
from time import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """execute async_comprehension
    four times in parallel using
    asyncio.gather. It also measure
    total runtime.
    """
    start_time = time()
    execute_async = [async_comprehension() for i in range(4)]
    result = await asyncio.gather(*execute_async)
    end_time = time()

    """ Total runtime explanation:
    - Total runtime is 10 seconds because it awaits 10
    asynchronous sleeps of 1 second each in the
    async_generator when calls are made to
    async_comprehension.
    """

    return end_time - start_time
