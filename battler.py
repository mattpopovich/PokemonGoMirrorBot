"""
This script will perform battles between two accounts.

Run this script as `python3 battler.py --lose` for the account that you want to lose with.
    First, go to the map, then pokeball (middle bottom), then pokemon. Have the top of this
        screen show the 3 pokemon you want to use in the battle. These should be
        very low CP pokemon, so I sort by CP (low at the top).
    Click on your avatar (bottom left), click on the desired friend that will win
        battles, then run this script.
You will also need to add the flag `--great`, `--ultra`, or `--master` for selecting which
    league that you want to battle in.
Ex. `python3 battler.py --lose --great`

Run this script as `python3 battler.py --win` for the account that you want to win with.
    Leave this account on the map screen, then run this script

Author: Matt Popovich (mattpopovich.com)
"""

# System imports
import datetime
import random
import time
import argparse
import sys

# Custom imports
import config
from cliclick import Cliclick
import functions.utils as utils

# Parse arguments
parser = argparse.ArgumentParser()
parser.add_argument(
    "-l",
    "--lose",
    help="When running the script, this account will win battles",
    action="store_true",
)
parser.add_argument(
    "-w",
    "--win",
    help="When running the script, this account will lose battles",
    action="store_true",
)
parser.add_argument(
    "-g", "--great", help="Perform battles in the great league", action="store_true"
)
parser.add_argument(
    "-u", "--ultra", help="Perform battles in the ultra league", action="store_true"
)
parser.add_argument(
    "-m", "--master", help="Perform battles in the master league", action="store_true"
)
args = parser.parse_args()

if not args.win and not args.lose:
    sys.exit("ERROR: must specify either --win or --lose argument")
elif args.win and args.lose:
    sys.exit("ERROR: can only specify one of --win or --lose arguments")

if args.great + args.ultra + args.master != 1:
    sys.exit("ERROR: must specify one of --great, --ultra, or --master")

# Access the coordinates from the active system
lets_do_it_coordinates = config.SETTINGS["lets_do_it_coordinates"]
start_battle_coordinates = config.SETTINGS["start_battle_coordinates"]
great_league_coordinates = config.SETTINGS["great_league_coordinates"]
ultra_league_coordinates = config.SETTINGS["ultra_league_coordinates"]
master_league_coordinates = config.SETTINGS["master_league_coordinates"]
lets_battle_coordinates = config.SETTINGS["lets_battle_coordinates"]
use_party_coordinates = config.SETTINGS["use_party_coordinates"]
rematch_coordinates = config.SETTINGS["rematch_coordinates"]
first_pokemon_in_party_coordinates = config.SETTINGS["first_pokemon_in_party_coordinates"]
first_pokemon_coordinates = config.SETTINGS["first_pokemon_coordinates"]
second_pokemon_coordinates = config.SETTINGS["second_pokemon_coordinates"]
third_pokemon_coordinates = config.SETTINGS["third_pokemon_coordinates"]
done_button_coordinates = config.SETTINGS["done_button_coordinates"]
change_prng = config.SETTINGS["change_prng"]

pixel_randomness = 10

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
cliclick.random_click(start_battle_coordinates, pixel_randomness)

# Use if have two different seeds for the two traders
#   (so that clicks won't be at the exact same time)
#   but still keep them in sync
setup_time_s = same_pseudo_rng.uniform(33, 38)
initial_setup_time_dt = datetime.datetime.now()
print(f"Planned setup time: {setup_time_s:.2f}s")

if args.lose:
    print(f"Clicking on start battle")
    cliclick.random_click(start_battle_coordinates, pixel_randomness)
    utils.random_sleep(3.0, 1.0)

    if args.great:
        print(f"Clicking on great league")
        cliclick.random_click(great_league_coordinates, pixel_randomness)
    elif args.ultra:
        print(f"Clicking on ultra league")
        cliclick.random_click(ultra_league_coordinates, pixel_randomness)
    elif args.master:
        print(f"Clicking on master league")
        cliclick.random_click(master_league_coordinates, pixel_randomness)
    utils.random_sleep(1.5, 0.75)

    print(f"Clicking on 'Let's Battle'")
    cliclick.random_click(lets_battle_coordinates, pixel_randomness)
    utils.random_sleep(2.0, 0.75)
else:
    print(f"Wait for other account create the battle")
    utils.random_sleep(11.0, 2.0)

    print(f"Clicking on 'Let's do it!'")
    cliclick.random_click(lets_do_it_coordinates, pixel_randomness)
    utils.random_sleep(4.5, 1.0)

num_battles = 12
for i in range(num_battles):
    if args.lose:
        print(f"Clicking on first pokemon in party")
        cliclick.random_click(first_pokemon_in_party_coordinates, pixel_randomness)
        utils.random_sleep(1.5, 0.75)

        print(f"Clicking on first pokemon")
        cliclick.random_click(first_pokemon_coordinates, pixel_randomness)
        utils.random_sleep(1.25, 0.5)

        print(f"Clicking on second pokemon")
        cliclick.random_click(second_pokemon_coordinates, pixel_randomness)
        utils.random_sleep(1.25, 0.5)

        print(f"Clicking on third pokemon")
        cliclick.random_click(third_pokemon_coordinates, pixel_randomness)
        utils.random_sleep(1.25, 0.5)

        print(f"Clicking on done button")
        cliclick.random_click(done_button_coordinates, pixel_randomness)
        utils.random_sleep(1.5, 0.75)

    print(f"Clicking on 'Use this party'")
    cliclick.random_click(use_party_coordinates, pixel_randomness)

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

    if args.win:
        print(f"Tapping to attack with first pokemon")
        cliclick.random_click(ultra_league_coordinates, pixel_randomness * 4)
        utils.random_sleep(15.0, 1.0)

        print(f"Tapping to attack with second pokemon")
        cliclick.random_click(ultra_league_coordinates, pixel_randomness * 4)
        utils.random_sleep(9.0, 2.0)

        print(f"Tapping to attack with third pokemon")
        cliclick.random_click(ultra_league_coordinates, pixel_randomness * 4)
        utils.random_sleep(11.0, 2.0)
    else:
        print(f"Clicking to get status of first loss")
        utils.random_sleep(2.0, 0.5)
        cliclick.random_click(ultra_league_coordinates, pixel_randomness * 4)
        utils.random_sleep(15.0, 1.0)

        print(f"Clicking to get status of second loss")
        cliclick.random_click(ultra_league_coordinates, pixel_randomness * 4)
        utils.random_sleep(9.0, 2.0)

        print(f"Clicking to get status of third loss")
        cliclick.random_click(ultra_league_coordinates, pixel_randomness * 4)
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
    cliclick.random_click(rematch_coordinates, pixel_randomness)
    utils.random_sleep(4.5, 1.0)
