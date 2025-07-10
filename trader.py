"""
This script will trade pokemon between two accounts

Get two accounts, go to their friends lists, click on each other,
    then run this script

Author: Matt Popovich (mattpopovich.com)
"""

# System imports
import random
import time
import datetime

# Custom imports
import config
from cliclick import Cliclick
import functions.utils as utils

# Access the coordinates from the active system
start_trade_coordinates = config.SETTINGS['start_trade_coordinates']
first_trade_pokemon_coordinates = config.SETTINGS['first_trade_pokemon_coordinates']
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
common_seed = int(now.strftime("%Y%m%d%H%M"))
print(f"Using common seed: {common_seed}")
same_pseudo_rng = random.Random(common_seed)

# Execute cliclick commands with randomized locations
cliclick = Cliclick()

# Make screen mirroring the "active" window
cliclick.click(utils.randomize_location(start_trade_coordinates, pixel_randomness))

num_trades = 35
for i in range(num_trades):
    print(f"Beginning trade {i+1}/{num_trades}")

    # Use if have two different seeds for the two traders
    #   (so that clicks won't be at the exact same time)
    #   but still keep them in sync
    remaining_sleep_s = same_pseudo_rng.uniform(45, 55)
    initial_remaining_sleep_s = remaining_sleep_s

    print(f"Clicking on start trade")
    cliclick.click(utils.randomize_location(start_trade_coordinates, pixel_randomness))
    remaining_sleep_s -= utils.random_sleep(7.0, 1.5)

    print("Clicking on first pokemon available to trade")
    cliclick.click(utils.randomize_location(first_trade_pokemon_coordinates, pixel_randomness))
    remaining_sleep_s -= utils.random_sleep(5.0, 1.5)

    print("Clicking on next")
    cliclick.click(utils.randomize_location(next_button_coordinates, pixel_randomness))
    remaining_sleep_s -= utils.random_sleep(5.0, 1.5)

    print("Clicking on confirm")
    cliclick.click(utils.randomize_location(confirm_button_coordinates, pixel_randomness))
    remaining_sleep_s -= utils.random_sleep(20.0, 1.5)

    print("Clicking on X")
    cliclick.click(utils.randomize_location(x_button_coordinates, pixel_randomness))
    remaining_sleep_s -= utils.random_sleep(5.0, 1.5)

    print(f"That trade took {(initial_remaining_sleep_s - remaining_sleep_s):.2f}s")
    print(f"Sleeping for {remaining_sleep_s:.2f}s to keep traders in sync\n")
    time.sleep(max(0, remaining_sleep_s))
