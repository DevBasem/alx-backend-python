#!/usr/bin/env python3
"""
Module for concurrent coroutines.
"""

import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Asynchronously spawns wait_random n times with specified max_delay.

    Args:
        n (int): Number of coroutines to spawn.
        max_delay (int): Maximum delay in seconds.

    Returns:
        List[float]: List of delays (float values) in ascending order.
    """
    delays = [wait_random(max_delay) for _ in range(n)]
    return [await delay for delay in asyncio.as_completed(delays)]
