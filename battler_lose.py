"""
This script will perform battles between two accounts.
Run this script for the account that you want to lose with.

First, go to the map, then pokeball (middle bottom), then pokemon. Have this
    screen show the top 3 pokemon you want to use in the battle. These should be
    very low CP pokemon, so I sort by CP (low at the top).
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
setup_time_s = same_pseudo_rng.uniform(33, 38)
initial_setup_time_dt = datetime.datetime.now()
print(f"Planned setup time: {setup_time_s:.2f}s")

print(f"Clicking on start battle")
cliclick.click(utils.randomize_location(start_battle_coordinates, pixel_randomness))
utils.random_sleep(3.0, 1.0)

print(f"Clicking on desired league to battle in")
cliclick.click(utils.randomize_location(ultra_league_coordiantes, pixel_randomness))
utils.random_sleep(1.5, 0.75)

print(f"Clicking on 'Let's Battle'")
cliclick.click(utils.randomize_location(lets_battle_coordinates, pixel_randomness))
utils.random_sleep(2.0, 0.75)

num_battles = 12
for i in range(num_battles):
    print(f"Clicking on first pokemon in party")
    cliclick.click(utils.randomize_location(first_pokemon_in_party_coordinates, pixel_randomness))
    utils.random_sleep(1.5, 0.75)

    print(f"Clicking on first pokemon")
    cliclick.click(utils.randomize_location(first_pokemon_coordinates, pixel_randomness))
    utils.random_sleep(1.25, 0.5)

    print(f"Clicking on second pokemon")
    cliclick.click(utils.randomize_location(second_pokemon_coordinates, pixel_randomness))
    utils.random_sleep(1.25, 0.5)

    print(f"Clicking on third pokemon")
    cliclick.click(utils.randomize_location(third_pokemon_coordinates, pixel_randomness))
    utils.random_sleep(1.25, 0.5)

    print(f"Clicking on done button")
    cliclick.click(utils.randomize_location(done_button_coordinates, pixel_randomness))
    utils.random_sleep(1.5, 0.75)

    print(f"Clicking on 'Use this party'")
    cliclick.click(utils.randomize_location(use_party_coordinates, pixel_randomness))

    finish_setup_time_dt = datetime.datetime.now()
    actual_setup_s = (finish_setup_time_dt - initial_setup_time_dt).total_seconds()
    post_setup_sleep_time_s = setup_time_s - actual_setup_s
    print(f"Setup took {(actual_setup_s):.2f}s")
    print(f"Sleeping for {post_setup_sleep_time_s:.2f}s to keep traders in sync\n")
    time.sleep(max(0, post_setup_sleep_time_s))

    print(f"Beginning battle {i+1}/{num_battles}")
    battle_length_s = same_pseudo_rng.uniform(42, 45)
    initial_battle_time_dt = datetime.datetime.now()
    print(f"Planned battle time: {battle_length_s:.2f}")

    print(f"Clicking to get status of first loss")
    utils.random_sleep(2.0, 0.5)
    cliclick.click(utils.randomize_location(ultra_league_coordiantes, pixel_randomness*4))
    utils.random_sleep(15.0, 1.0)

    print(f"Clicking to get status of second loss")
    cliclick.click(utils.randomize_location(ultra_league_coordiantes, pixel_randomness*4))
    utils.random_sleep(9.0, 2.0)

    print(f"Clicking to get status of third loss")
    cliclick.click(utils.randomize_location(ultra_league_coordiantes, pixel_randomness*4))
    utils.random_sleep(11.0, 2.0)

    finish_battle_time_dt = datetime.datetime.now()
    actual_battle_s = (finish_battle_time_dt - initial_battle_time_dt).total_seconds()
    post_battle_sleep_time_s = battle_length_s - actual_battle_s
    print(f"Battle took {actual_battle_s:.2f}s")
    print(f"Sleeping for {post_battle_sleep_time_s:.2f}s to keep traders in sync\n")
    time.sleep(max(0, post_battle_sleep_time_s))

    setup_time_s = same_pseudo_rng.uniform(25, 30)
    initial_setup_time_dt = datetime.datetime.now()
    print(f"Planned setup time: {setup_time_s:.2f}s")

    print(f"Tapping on rematch")
    cliclick.click(utils.randomize_location(rematch_coordinates, pixel_randomness))
    utils.random_sleep(2.0, 0.75)

