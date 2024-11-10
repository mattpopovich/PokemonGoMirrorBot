"""
Get two accounts, go to their friends lists, click on each other,
    then run this script
Author: Matt Popovich (mattpopovich.com)
"""


import random
import time
import subprocess
import config
from cliclick import Cliclick
import datetime


def randomize_location(location, pixel_randomness):
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

def random_sleep(base_sleep_time_s, randomness_s):
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

# Access the coordinates from the active system
start_trade_coordinates = config.SETTINGS['start_trade_coordinates']
first_pokemon_coordinates = config.SETTINGS['first_pokemon_coordinates']
next_button_coordinates = config.SETTINGS['next_button_coordinates']
confirm_button_coordinates = config.SETTINGS['confirm_button_coordinates']
x_button_coordinates = config.SETTINGS['x_button_coordinates']
change_delay = config.SETTINGS['change_delay']

pixel_randomness = 10

# Get the current date and time up to the current minute
now = datetime.datetime.now().replace(second=0, microsecond=0)

# Convert it to a seed value
seed_value = int(now.strftime("%Y%m%d%H%M"))  # e.g., 202411081231 for Nov 8, 2024, 12:31

# Use the seed value for random operations
modified_seed = seed_value + 1 if change_delay else seed_value
random.seed(modified_seed)
# A common PRNG between traders
same_pseudo_rng = random.Random(int(now.strftime("%Y%m%d%H%M")))

# Execute cliclick commands with randomized locations
cliclick = Cliclick()

# Make screen mirroring the "active" window
cliclick.click(randomize_location(start_trade_coordinates, pixel_randomness))

for _ in range(40):

    # Use if have two different seeds for the two traders
    #   (so that clicks won't be at the exact same time)
    #   but still keep them in sync
    remaining_sleep = same_pseudo_rng.uniform(40, 50)
    initial_remaining_sleep = remaining_sleep

    print(f"Clicking on start trade")
    cliclick.click(randomize_location(start_trade_coordinates, pixel_randomness))
    remaining_sleep -= random_sleep(7.0, 1.5)

    print("Clicking on first pokemon available to trade")
    cliclick.click(randomize_location(first_pokemon_coordinates, pixel_randomness))
    remaining_sleep -= random_sleep(4.0, 1.5)

    print("Clicking on next")
    cliclick.click(randomize_location(next_button_coordinates, pixel_randomness))
    remaining_sleep -= random_sleep(5.0, 1.5)

    print("Clicking on confirm")
    cliclick.click(randomize_location(confirm_button_coordinates, pixel_randomness))
    remaining_sleep -= random_sleep(20.0, 1.5)

    print("Clicking on X")
    cliclick.click(randomize_location(x_button_coordinates, pixel_randomness))
    remaining_sleep -= random_sleep(5.0, 1.5)

    print(f"That trade took {(initial_remaining_sleep - remaining_sleep):.2f}s")
    print(f"Sleeping for {remaining_sleep:.2f}s to keep traders in sync\n")
    time.sleep(max(0, remaining_sleep))
