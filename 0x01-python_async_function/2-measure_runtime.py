#!/usr/bin/env python3
"""
Module for measuring runtime.
"""

import time
import asyncio
from typing import Callable


def measure_time(n: int, max_delay: int) -> float:
    """
    Measures the total execution time for wait_n(n, max_delay),
    and returns total_time / n.

    Args:
        n (int): Number of coroutines to spawn.
        max_delay (int): Maximum delay in seconds.

    Returns:
        float: Average execution time per coroutine.
    """
    start_time = time.time()
    wait_n = __import__('1-concurrent_coroutines').wait_n
    asyncio.run(wait_n(n, max_delay))
    end_time = time.time()
    total_time = end_time - start_time
    return total_time / n
