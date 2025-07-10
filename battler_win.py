"""
This script will perform battles between two accounts.
Run this script for the account that you want to win with.

Leave this account on the map screen, then run this script

Author: Matt Popovich (mattpopovich.com)
"""

# System imports
import datetime
import random
import time

# Custom imports
import config
from cliclick import Cliclick
import functions.utils as utils


# Access the coordinates from the active system
lets_do_it_coordinates = config.SETTINGS['lets_do_it_coordinates']
start_battle_coordinates = config.SETTINGS['start_battle_coordinates']
ultra_league_coordiantes = config.SETTINGS['ultra_league_coordinates']
lets_battle_coordinates = config.SETTINGS['lets_battle_coordinates']
use_party_coordinates = config.SETTINGS['use_party_coordinates']
rematch_coordinates = config.SETTINGS['rematch_coordinates']
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
cliclick.click(utils.randomize_location(start_battle_coordinates, pixel_randomness))

# Use if have two different seeds for the two traders
#   (so that clicks won't be at the exact same time)
#   but still keep them in sync
remaining_sleep_s = same_pseudo_rng.uniform(33, 38)
initial_remaining_sleep_s = remaining_sleep_s
print(f"Setup time: {initial_remaining_sleep_s:.2f}s")

print(f"Wait for other account create the battle")
remaining_sleep_s -= utils.random_sleep(11.0, 2.0)

print(f"Clicking on 'Let's do it!'")
cliclick.click(utils.randomize_location(lets_do_it_coordinates, pixel_randomness))
remaining_sleep_s -= utils.random_sleep(3.0, 1.0)

print(f"Clicking on 'Use this party'")
cliclick.click(utils.randomize_location(use_party_coordinates, pixel_randomness))
remaining_sleep_s -= utils.random_sleep(3.0, 1.0)


num_battles = 5
for i in range(num_battles):
    print(f"Setup took {(initial_remaining_sleep_s - remaining_sleep_s):.2f}s")
    print(f"Sleeping for {remaining_sleep_s:.2f}s to keep traders in sync\n")
    time.sleep(max(0, remaining_sleep_s))

    print(f"Beginning battle {i+1}/{num_battles}")
    remaining_sleep_s = same_pseudo_rng.uniform(42, 45)
    initial_remaining_sleep_s = remaining_sleep_s

    print(f"Tapping to attack with first pokemon")
    cliclick.click(utils.randomize_location(ultra_league_coordiantes, pixel_randomness*4))
    remaining_sleep_s -= utils.random_sleep(15.0, 1.0)

    print(f"Tapping to attack with second pokemon")
    cliclick.click(utils.randomize_location(ultra_league_coordiantes, pixel_randomness*4))
    remaining_sleep_s -= utils.random_sleep(9.0, 2.0)

    print(f"Tapping to attack with third pokemon")
    cliclick.click(utils.randomize_location(ultra_league_coordiantes, pixel_randomness*4))
    remaining_sleep_s -= utils.random_sleep(11.0, 2.0)

    print(f"Battle took {(initial_remaining_sleep_s - remaining_sleep_s):.2f}s")
    print(f"Sleeping for {remaining_sleep_s:.2f}s to keep traders in sync\n")
    time.sleep(max(0, remaining_sleep_s))

    remaining_sleep_s = same_pseudo_rng.uniform(25, 30)
    initial_remaining_sleep_s = remaining_sleep_s
    print(f"Setup time: {initial_remaining_sleep_s:.2f}s")

    print(f"Tapping on rematch")
    cliclick.click(utils.randomize_location(rematch_coordinates, pixel_randomness))
    remaining_sleep_s -= utils.random_sleep(2.0, 0.75)

    print(f"Clicking on 'Use this party'")
    cliclick.click(utils.randomize_location(use_party_coordinates, pixel_randomness))

