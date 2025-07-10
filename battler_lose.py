"""
This script will perform battles between two accounts.
Run this script for the account that you want to lose with.

Click on your avatar (bottom left), click on the desired friend that will win
    battles, then run this script.

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
start_battle_coordinates = config.SETTINGS['start_battle_coordinates']
great_league_coordiantes = config.SETTINGS['great_league_coordinates']
ultra_league_coordiantes = config.SETTINGS['ultra_league_coordinates']
master_league_coordiantes = config.SETTINGS['master_league_coordinates']
lets_battle_coordinates = config.SETTINGS['lets_battle_coordinates']
use_party_coordinates = config.SETTINGS['use_party_coordinates']
rematch_coordinates = config.SETTINGS['rematch_coordinates']
first_pokemon_in_party_coordinates = config.SETTINGS['first_pokemon_in_party_coordinates']
sort_button_coordinates = config.SETTINGS['sort_button_coordinates']
first_pokemon_coordinates = config.SETTINGS['first_pokemon_coordinates']
second_pokemon_coordinates = config.SETTINGS['second_pokemon_coordinates']
third_pokemon_coordinates = config.SETTINGS['third_pokemon_coordinates']
done_button_coordinates = config.SETTINGS['done_button_coordinates']
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
remaining_sleep_s = same_pseudo_rng.uniform(22, 30)
initial_remaining_sleep_s = remaining_sleep_s


print(f"Clicking on start battle")
cliclick.click(utils.randomize_location(start_battle_coordinates, pixel_randomness))
remaining_sleep_s -= utils.random_sleep(3.0, 1.0)

print(f"Clicking on great league")
cliclick.click(utils.randomize_location(great_league_coordiantes, pixel_randomness))
remaining_sleep_s -= utils.random_sleep(1.5, 0.75)

print(f"Clicking on 'Let's Battle'")
cliclick.click(utils.randomize_location(lets_battle_coordinates, pixel_randomness))
remaining_sleep_s -= utils.random_sleep(2.0, 0.75)

num_battles = 5
for i in range(num_battles):
    print(f"Clicking on first pokemon in party")
    cliclick.click(utils.randomize_location(first_pokemon_in_party_coordinates, pixel_randomness))
    remaining_sleep_s -= utils.random_sleep(1.5, 0.75)

    print(f"Clicking on sort button")
    cliclick.click(utils.randomize_location(sort_button_coordinates, pixel_randomness))
    remaining_sleep_s -= utils.random_sleep(1.5, 0.75)

    print(f"Selecting CP to sort low at the top")
    cliclick.click(utils.randomize_location(sort_button_coordinates, pixel_randomness))
    remaining_sleep_s -= utils.random_sleep(1.5, 0.75)

    print(f"Clicking on first pokemon")
    cliclick.click(utils.randomize_location(first_pokemon_coordinates, pixel_randomness))
    remaining_sleep_s -= utils.random_sleep(1.0, 0.75)

    print(f"Clicking on second pokemon")
    cliclick.click(utils.randomize_location(second_pokemon_coordinates, pixel_randomness))
    remaining_sleep_s -= utils.random_sleep(1.0, 0.75)

    print(f"Clicking on third pokemon")
    cliclick.click(utils.randomize_location(third_pokemon_coordinates, pixel_randomness))
    remaining_sleep_s -= utils.random_sleep(1.0, 0.75)

    print(f"Clicking on done button")
    cliclick.click(utils.randomize_location(done_button_coordinates, pixel_randomness))
    remaining_sleep_s -= utils.random_sleep(1.5, 0.75)

    print(f"Clicking on 'Use this party'")
    cliclick.click(utils.randomize_location(use_party_coordinates, pixel_randomness))
    remaining_sleep_s -= utils.random_sleep(16.0, 1.0)

    print(f"Setup took {(initial_remaining_sleep_s - remaining_sleep_s):.2f}s")
    print(f"Sleeping for {remaining_sleep_s:.2f}s to keep traders in sync\n")
    time.sleep(max(0, remaining_sleep_s))


    remaining_sleep_s = same_pseudo_rng.uniform(65, 70)
    initial_remaining_sleep_s = remaining_sleep_s

    print(f"Clicking to get status of first loss")
    remaining_sleep_s -= utils.random_sleep(1.0, 1.0)
    cliclick.click(utils.randomize_location(ultra_league_coordiantes, pixel_randomness*4))
    remaining_sleep_s -= utils.random_sleep(15.8, 1.0)

    print(f"Clicking to get status of second loss")
    cliclick.click(utils.randomize_location(ultra_league_coordiantes, pixel_randomness*4))
    remaining_sleep_s -= utils.random_sleep(9.0, 2.0)

    print(f"Clicking to get status of third loss")

    print(f"Tapping on rematch")
    cliclick.click(utils.randomize_location(rematch_coordinates, pixel_randomness))
    remaining_sleep_s -= utils.random_sleep(2.0, 0.75)

    print(f"Battle took {(initial_remaining_sleep_s - remaining_sleep_s):.2f}s")
    print(f"Sleeping for {remaining_sleep_s:.2f}s to keep traders in sync\n")
    time.sleep(max(0, remaining_sleep_s))
