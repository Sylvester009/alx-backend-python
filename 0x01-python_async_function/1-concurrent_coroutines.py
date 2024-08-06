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
    task_list = []  # init empty list to store delayed tasks
    tasks = [wait_random(max_delay) for _ in range(n)]
    completed_tasks = asyncio.as_completed(tasks)
    for task in completed_tasks:
        result = await task
        task_list.append(result)
    return task_list
