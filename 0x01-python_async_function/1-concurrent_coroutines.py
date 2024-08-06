#!/usr/bin/env python3

"""
an async routine called wait_n
that takes in 2 int arguments
(in this order): n and max_delay
"""

import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """create a list of tasks, then gather and
    sort them before returning it
    """
    tasks = [wait_random(max_delay) for _ in range(n)]
    delayed_tasks = await asyncio.gather(*tasks)

    for i in range(len(delayed_tasks)):
        for j in range(len(delayed_tasks) - i - 1):
            if delayed_tasks[j] > delayed_tasks[j + 1]:
                delayed_tasks[j], delayed_Tasks[j + 1]
                = delayed_tasks[j + 1], delayed_tasks[j]

    return delayed_tasks
