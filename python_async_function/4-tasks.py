#!/usr/bin/env python3
"""Spawn task_wait_random n times and return sorted delays."""

import asyncio
import bisect
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawn task_wait_random n times with given max_delay
and return sorted delays.
    ...
        List[float]: List of delays in ascending order.
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    delays = []

    for task in asyncio.as_completed(tasks):
        delay = await task
        bisect.insort(delays, delay)

    return delays
