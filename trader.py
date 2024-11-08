import random
import time
import subprocess
import config
from cliclick import Cliclick
import datetime


def randomize_location(location, randomness):
    """
    Randomizes the location coordinates within a specified randomness range.

    Args:
    - location (list): A list in the form [x, y].
    - randomness (int): Range of random offset for both x and y.

    Returns:
    - list: New randomized location as [new_x, new_y].
    """
    location_x, location_y = location
    random_offset_x = random.randint(-randomness, randomness)
    random_offset_y = random.randint(-randomness, randomness)

    new_x = location_x + random_offset_x
    new_y = location_y + random_offset_y

    return [new_x, new_y]

def random_sleep(base_sleep_time, randomness):
    """
    Sleeps for a random duration based on base sleep time and randomness range.

    Args:
    - base_sleep_time (float): Base sleep time in seconds.
    - randomness (float): Maximum random offset in seconds.

    Returns:
    - float: The actual sleep time.
    """
    offset = random.uniform(-randomness, randomness)
    actual_sleep_time = max(0, base_sleep_time + offset)

    print(f"  Sleeping for {actual_sleep_time}")
    time.sleep(actual_sleep_time)

    return actual_sleep_time

# Access the coordinates from the active system
startTrade = config.ACTIVE_COORDINATES['startTrade']
bottomCenterPokemon = config.ACTIVE_COORDINATES['bottomCenterPokemon']
next_button = config.ACTIVE_COORDINATES['next_button']
confirm = config.ACTIVE_COORDINATES['confirm']
x = config.ACTIVE_COORDINATES['x']

randomness = 10

# Get the current date and time up to the current minute
now = datetime.datetime.now().replace(second=0, microsecond=0)

# Convert it to a seed value
seed_value = int(now.strftime("%Y%m%d%H%M"))  # e.g., 202411081231 for Nov 8, 2024, 12:31

# Use the seed value for random operations
modified_seed = seed_value    # Optional if you want to modify seeds between traders
random.seed(modified_seed)
same_pseudo_rng = random.Random(int(now.strftime("%Y%m%d%H%M")))

# Execute cliclick commands with randomized locations
cliclick = Cliclick()
cliclick.click(randomize_location(startTrade, randomness))

for _ in range(10):

    # Use if have two different seeds for the two traders
    #   (so that clicks won't be at the exact same time)
    #   but still keep them in sync
    remaining_sleep = same_pseudo_rng.uniform(45, 55)

    print(f"Clicking on start trade")
    cliclick.click(randomize_location(startTrade, randomness))
    remaining_sleep -= random_sleep(7.0, 2.0)

    print("Clicking on bottom center pokemon")
    cliclick.click(randomize_location(bottomCenterPokemon, randomness))
    remaining_sleep -= random_sleep(4.0, 2.0)

    print("Clicking on next")
    cliclick.click(randomize_location(next_button, randomness))
    remaining_sleep -= random_sleep(5.0, 2.0)

    print("Clicking on confirm")
    cliclick.click(randomize_location(confirm, randomness))
    remaining_sleep -= random_sleep(18.0, 2.0)

    print("Clicking on X")
    cliclick.click(randomize_location(x, randomness))
    remaining_sleep -= random_sleep(5.0, 2.0)

    print(f"Sleeping for {remaining_sleep} to keep traders in sync")
    time.sleep(max(0, remaining_sleep))
