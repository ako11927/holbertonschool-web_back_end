#!/usr/bin/env python3
"""Measure the runtime of wait_n."""

import time
import asyncio
from typing import List
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measure total execution time for wait_n(n, max_delay) and return average.

    Args:
        n (int): Number of times to spawn wait_random.
        max_delay (int): Maximum delay for each call.

    Returns:
        float: Average time per iteration (total_time / n).
    """
    start = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    end = time.perf_counter()
    total_time = end - start
    return total_time / n
