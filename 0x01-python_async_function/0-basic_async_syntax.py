#!/usr/bin/env python3
"""
Async basics
"""

import random

try:
    import asyncio
except ImportError:
    # For Python 2.7.12 compatibility
    import trollius as asyncio

@asyncio.coroutine
def wait_random(max_delay=10):
    """
    Asynchronous coroutine that waits for a random delay
    between 0 and max_delay seconds and eventually returns it.

    Args:
        max_delay (int): Maximum delay (default 10)

    Returns:
        float: Random delay
    """
    delay = random.uniform(0, max_delay)
    yield from asyncio.sleep(delay)
    return delay

def run(coroutine):
    if hasattr(asyncio, "run"):
        return asyncio.run(coroutine)
    else:
        loop = asyncio.get_event_loop()
        try:
            return loop.run_until_complete(coroutine)
        finally:
            loop.close()
