#!/usr/bin/env python3
"""
Module for tasks.
"""

import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Asynchronously spawns task_wait_random n times with specified max_delay.

    Args:
        n (int): Number of coroutines to spawn.
        max_delay (int): Maximum delay in seconds.

    Returns:
        List[float]: List of delays (float values) in ascending order.
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    return [await task for task in asyncio.as_completed(tasks)]
