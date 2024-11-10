"""
This script will scroll through pokemon and modify their favorite status
Ex. Given a list of tags, open the first pokemon, and run this script

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
start_drag_next_poke = config.SETTINGS['start_drag_next_poke']
end_drag_next_poke = config.SETTINGS['end_drag_next_poke']
modify_favorite = config.SETTINGS['modify_favorite']

pixel_randomness = 10

# How many pixels offset could we start our drag from
#   This is the offset in the up direction but also in the down direction, 
#   effectively doubling its randomness
drag_randomness_y = 100


# Get the current date and time
now = datetime.datetime.now()

# Convert it to a seed value
seed_value = int(now.strftime("%Y%m%d%H%M%S%f"))  # e.g., 20241109192333378839 for Nov 9, 2024, 7:23:33.3378839 PM UTC

# Use the seed value for random operations
random.seed(seed_value)

# Execute cliclick commands with randomized locations
cliclick = Cliclick()

# Make screen mirroring the "active" window
cliclick.click(randomize_location(start_drag_next_poke, pixel_randomness))

for _ in range(1500):

    # How long will it take to modify favorite and move to next pokemon
    remaining_sleep = random.uniform(1, 2)
    initial_remaining_sleep = remaining_sleep

    print(f"Clicking to modify favorite")
    cliclick.click(randomize_location(modify_favorite, pixel_randomness))
    remaining_sleep -= random_sleep(.5, .2)

    print("Clicking to start drag")
    random_start_location = randomize_location(start_drag_next_poke, pixel_randomness)
    cliclick.start_drag(random_start_location)
    remaining_sleep -= random_sleep(.05, .01)

    # Drag cursor
    num_drags = 15
    max_slope = pow(drag_randomness_y, 1/num_drags)
    slope = random.uniform(-max_slope, max_slope)
    random_end_location = randomize_location(end_drag_next_poke, pixel_randomness)
    
    total_movement_x = random_start_location[0] - random_end_location[0]
    per_movement_x = total_movement_x / num_drags + random.randint(-3, 3)
    slope_y = 1 if slope > 0 else -1

    sleep_per_drag = random.uniform(.05/num_drags, .02)
    
    for j in range(num_drags):
        next_location_x = random_start_location[0] - (per_movement_x*(j+1))
        per_movement_y = abs(pow(slope, j))
        next_location_y =  random_start_location[1] + slope_y * per_movement_y

        next_location = [int(next_location_x), int(next_location_y)]
        print(f"Dragging cursor part {j+1}/{num_drags}")
        cliclick.continue_drag(next_location)

        time.sleep(sleep_per_drag)
        remaining_sleep -= sleep_per_drag

    print("Finishing drag")
    cliclick.release_drag(next_location)
    remaining_sleep -= random_sleep(.2, .1)

    print(f"Modifying that favorite took {(initial_remaining_sleep - remaining_sleep):.2f}s")
    print(f"Sleeping for {remaining_sleep:.2f}s to cool down\n")
    time.sleep(max(0.15, remaining_sleep))
