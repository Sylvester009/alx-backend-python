#!/usr/bin/env python3

import asyncio
import random

"""
an asynchronous coroutine that takes
in an integer argument and eventually
returns it
"""


async def wait_random(max_delay: int = 10) -> float:
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
