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
import sys

# Custom imports
import config
from cliclick import Cliclick
import functions.utils as utils

def ensure_correct_screen(expected_color: list[int], coordinates: list[int], tolerance: int = 0):
    """
    This function ensures that you are currently on the expected screen
    If not, the program will exit

    color = [255, 255, 255]

    There are some rare cases where this does not work, Ex. large shadow pokemon
    """
    num_attempts = 1
    # Sometimes we are at the right screen but the color is just a little bit off
    for i in range(num_attempts):
        print("Taking screenshot...")
        color_str: str = cliclick.get_color(coordinates)
        color: list[int] = list(map(int, color_str.split()))
        if rgb_values_close(color, expected_color, tolerance):
            print(f"Expected color {expected_color} and was {color}. Within {toler}")
            return
        else:
            print(f"Expected color {expected_color} but was {color}... retrying")
            time.sleep(1.0)

    sys.exit(f"Likely not at Pokemon details screen, script may have failed. "
                 f"Expected color {expected_color} but was {color}")

def rgb_values_close(rgb1, rgb2, tolerance):
    """
    Checks if two RGB values are close within a given tolerance.

    :param rgb1: List or tuple representing the first RGB value [R, G, B]
    :param rgb2: List or tuple representing the second RGB value [R, G, B]
    :param tolerance: Allowed difference for each channel
    :return: True if all channels are within the tolerance, False otherwise
    """
    return all(abs(a - b) <= tolerance for a, b in zip(rgb1, rgb2))

# Access the coordinates from the active system
SCREEN_CAPTURE_ALWAYS = config.SCREEN_CAPTURE_ALWAYS
SCREEN_CAPTURE_MINIMAL = config.SCREEN_CAPTURE_MINIMAL

start_trade_coordinates = config.SETTINGS['start_trade_coordinates']
first_trade_pokemon_coordinates = config.SETTINGS['first_trade_pokemon_coordinates']
between_first_second_pokemon = config.SETTINGS['between_first_second_pokemon']
next_button_coordinates = config.SETTINGS['next_button_coordinates']
confirm_button_coordinates = config.SETTINGS['confirm_button_coordinates']
pokemon_details_left_health_white = config.SETTINGS['pokemon_details_left_health_white']
x_button_coordinates = config.SETTINGS['x_button_coordinates']
change_prng = config.SETTINGS['change_prng']

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
    remaining_sleep_s = same_pseudo_rng.uniform(46, 55)
    initial_remaining_sleep_s = remaining_sleep_s

    print(f"Clicking on start trade")
    if SCREEN_CAPTURE_ALWAYS:
        ensure_correct_screen([255, 255, 255], next_button_coordinates, 3)
    cliclick.random_click(start_trade_coordinates, pixel_randomness)
    remaining_sleep_s -= utils.random_sleep(8.0, 1.5)

    print("Clicking on first pokemon available to trade")
    if SCREEN_CAPTURE_ALWAYS:
        # Wait until between first second poke is not +-10 of 93 173 241
        # Wait until between first second poke +-10 of 255 255 255
        ensure_correct_screen([253, 255, 251], between_first_second_pokemon, 10)
    cliclick.random_click(first_trade_pokemon_coordinates, pixel_randomness)
    remaining_sleep_s -= utils.random_sleep(5.0, 1.5)

    print("Clicking on next")
    if SCREEN_CAPTURE_ALWAYS:
        # Wait until next button +-10 from 106 207 150
        ensure_correct_screen([97, 177, 241], confirm_button_coordinates, 5)
    cliclick.random_click(next_button_coordinates, pixel_randomness)
    remaining_sleep_s -= utils.random_sleep(5.0, 1.5)

    print("Clicking on confirm")
    if SCREEN_CAPTURE_ALWAYS or SCREEN_CAPTURE_MINIMAL:
        ensure_correct_screen([126, 184, 241], first_pokemon_coordinates, 5)
    cliclick.random_click(confirm_button_coordinates, pixel_randomness)
    remaining_sleep_s -= utils.random_sleep(20.0, 1.5)
    utils.log_trade(LOG_FILE)

    print("Clicking on X")
    if SCREEN_CAPTURE_ALWAYS:
        ensure_correct_screen([255, 255, 255], pokemon_details_left_health_white, 0)
    cliclick.random_click(x_button_coordinates, pixel_randomness)
    remaining_sleep_s -= utils.random_sleep(5.0, 1.5)

    print(f"That trade took {(initial_remaining_sleep_s - remaining_sleep_s):.2f}s")
    print(f"Sleeping for {remaining_sleep_s:.2f}s to keep traders in sync\n")
    time.sleep(max(0, remaining_sleep_s))
