#!/usr/bin/env python3
"""Create an asyncio Task for wait_random."""

import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Create an asyncio Task for wait_random with the given max_delay.

    Args:
        max_delay (int): Maximum delay for wait_random.

    Returns:
        asyncio.Task: A task that runs wait_random(max_delay).
    """
    return asyncio.create_task(wait_random(max_delay))
