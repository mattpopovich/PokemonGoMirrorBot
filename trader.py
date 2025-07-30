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
from functions.cliclick import Cliclick
import functions.utils as utils

# Access the coordinates from the active system
start_trade_coordinates = config.SETTINGS["start_trade_coordinates"]
first_trade_pokemon_coordinates = config.SETTINGS["first_trade_pokemon_coordinates"]
next_button_coordinates = config.SETTINGS["next_button_coordinates"]
confirm_button_coordinates = config.SETTINGS["confirm_button_coordinates"]
x_button_coordinates = config.SETTINGS["x_button_coordinates"]
change_prng = config.SETTINGS["change_prng"]

pixel_randomness = 10
LOG_FILE = "trader_log.txt"

# Get the current date and time up to the current minute
now = datetime.datetime.now().replace(second=0, microsecond=0)

# Convert it to a seed value
seed_value = int(now.strftime("%Y%m%d%H%M"))  # e.g., 202411081231 for Nov 8, 2024, 12:31

# Use the seed value for random operations
modified_seed = seed_value + 1 if change_prng else seed_value
random.seed(modified_seed)
# A common PRNG between traders
common_seed = int(now.strftime("%Y%m%d%H%M"))
print(f"Using common seed: {common_seed}")
same_pseudo_rng = random.Random(common_seed)

# Execute cliclick commands with randomized locations
cliclick = Cliclick()

# Make screen mirroring the "active" window
cliclick.random_click(start_trade_coordinates, pixel_randomness)

num_trades = 35
for i in range(num_trades):
    print(f"Beginning trade {i+1}/{num_trades}")
    num_trades_since_midnight, num_total_trades = utils.get_trade_counts(LOG_FILE)
    print(f"\t{num_trades_since_midnight} trades made today, {num_total_trades} all time")

    # Use if have two different seeds for the two traders
    #   (so that clicks won't be at the exact same time)
    #   but still keep them in sync
    trade_time_with_sleep_s = same_pseudo_rng.uniform(46, 55)
    start_trade_dt = datetime.datetime.now()

    print(f"Clicking on start trade")
    cliclick.random_click(start_trade_coordinates, pixel_randomness)
    utils.random_sleep(8.0, 1.5)

    print("Clicking on first pokemon available to trade")
    cliclick.random_click(first_trade_pokemon_coordinates, pixel_randomness)
    utils.random_sleep(5.0, 1.5)

    print("Clicking on next")
    cliclick.random_click(next_button_coordinates, pixel_randomness)
    utils.random_sleep(5.0, 1.5)

    print("Clicking on confirm")
    cliclick.random_click(confirm_button_coordinates, pixel_randomness)
    utils.random_sleep(20.0, 1.5)
    utils.log_trade(LOG_FILE)

    print("Clicking on X")
    cliclick.random_click(x_button_coordinates, pixel_randomness)
    utils.random_sleep(5.0, 1.5)

    finish_trade_dt = datetime.datetime.now()
    trade_length_s = (finish_trade_dt - start_trade_dt).total_seconds()
    post_trade_sleep_time_s = trade_time_with_sleep_s - trade_length_s
    print(f"That trade took {trade_length_s:.2f}s")
    print(f"Sleeping for {post_trade_sleep_time_s:.2f}s to keep traders in sync\n")
    time.sleep(max(0, post_trade_sleep_time_s))
