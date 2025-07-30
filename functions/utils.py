"""
Functions used throughout PokemonGoMirrorBot

Author: Matt Popovich (mattpopovich.com)
"""

import random
import time
from datetime import datetime


def randomize_location(location: list[int], pixel_randomness: int) -> list[int]:
    """
    Randomizes the location coordinates within a specified pixel_randomness range.

    Args:
    - location (list): A list in the form [x, y].
    - pixel_randomness (int): Maximum random offset for both x and y.

    Returns:
    - list: New randomized location as [new_x, new_y].
    """
    location_x, location_y = location
    random_offset_x = random.randint(-pixel_randomness, pixel_randomness)
    random_offset_y = random.randint(-pixel_randomness, pixel_randomness)

    new_x = location_x + random_offset_x
    new_y = location_y + random_offset_y

    return [new_x, new_y]


def random_sleep(
    base_sleep_time_s: float, randomness_s: float, unittest: bool = False
) -> float:
    """
    Sleeps for a random duration based on base sleep time and randomness_s range.

    Args:
    - base_sleep_time_s (float): Base sleep time in seconds.
    - randomness_s (float): Maximum random offset in seconds.

    Returns:
    - float: The actual sleep time.
    """
    offset = random.uniform(-randomness_s, randomness_s)
    actual_sleep_time = max(0, base_sleep_time_s + offset)

    if not unittest:
        print(f"  Sleeping for {actual_sleep_time:.2f}s")
        time.sleep(actual_sleep_time)

    return actual_sleep_time


def log_trade(filename: str) -> None:
    """Logs the current date and time to a trades log file."""
    now = datetime.now()
    with open(filename, "a") as f:
        f.write(f"{now.isoformat()}\n")


def get_trade_counts(filename: str) -> tuple[int, int]:
    """
    Returns a tuple with the number of trades since midnight and the total number of trades.
    If the log file does not exist, returns (0, 0).
    """
    trades_total = 0
    trades_since_midnight = 0
    today = datetime.now().date()

    try:
        with open(filename, "r") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue  # skip empty lines
                try:
                    dt = datetime.fromisoformat(line)
                    trades_total += 1
                    if dt.date() == today:
                        trades_since_midnight += 1
                except ValueError:
                    # Skip lines that aren't valid ISO 8601 timestamps
                    continue
    except FileNotFoundError:
        print(
            f"WARNING: Log file {filename} does not exist. This is expected if this is the first run."
        )
        return 0, 0

    return trades_since_midnight, trades_total
