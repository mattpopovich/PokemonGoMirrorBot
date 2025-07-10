"""
Functions used throughout PokemonGoMirrorBot

Author: Matt Popovich (mattpopovich.com)
"""

import random
import time

def randomize_location(location: list[int], pixel_randomness: int):
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

def random_sleep(base_sleep_time_s: float, randomness_s: float):
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

    print(f"  Sleeping for {actual_sleep_time:.2f}s")
    time.sleep(actual_sleep_time)

    return actual_sleep_time