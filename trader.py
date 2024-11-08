import random
import time
import subprocess
import config

seed = 12345
random.seed(seed)

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
    global seed
    seed += 1
    random.seed(seed)
    
    offset = random.uniform(-randomness, randomness)
    actual_sleep_time = max(0, base_sleep_time + offset)
    
    time.sleep(actual_sleep_time)
    
    return actual_sleep_time

def cliclick(command):
    """
    Executes the cliclick command in the terminal.
    
    Args:
    - command (str): The cliclick command to be executed.
    """
    try:
        subprocess.run(["cliclick", command], check=True)
        print(f"executed {command}")
    except subprocess.CalledProcessError as e:
        print(f"Error executing cliclick command: {e}")

def format_command(location):
    """
    Formats the location list into a string command for cliclick.
    
    Args:
    - location (list): The location as [x, y].
    
    Returns:
    - str: The formatted command for cliclick.
    """
    return f"c:{location[0]},{location[1]}"

# Access the coordinates from the active system
startTrade = config.ACTIVE_COORDINATES['startTrade']
bottomCenterPokemon = config.ACTIVE_COORDINATES['bottomCenterPokemon']
next_button = config.ACTIVE_COORDINATES['next_button']
confirm = config.ACTIVE_COORDINATES['confirm']
x = config.ACTIVE_COORDINATES['x']

randomness = 10

# Execute cliclick commands with randomized locations
cliclick(format_command(randomize_location(startTrade, randomness)))

for _ in range(10):

    # Use if you want to have two different seeds for the two traders but 
    #   still keep them in sync
    remaining_sleep = 35.0
    
    print(f"Clicking on start trade")
    cliclick(format_command(randomize_location(startTrade, randomness)))
    remaining_sleep -= random_sleep(7.0, 2.0)
    
    print("Clicking on bottom center pokemon")
    cliclick(format_command(randomize_location(bottomCenterPokemon, randomness)))
    remaining_sleep -= random_sleep(4.0, 2.0)
    
    print("clicking on next")
    cliclick(format_command(randomize_location(next_button, randomness)))
    remaining_sleep -= random_sleep(5.0, 2.0)
    
    print("clicking on confirm")
    cliclick(format_command(randomize_location(confirm, randomness)))
    remaining_sleep -= random_sleep(18.0, 2.0)
    
    print("clicking on X")
    cliclick(format_command(randomize_location(x, randomness)))
    remaining_sleep -= random_sleep(5.0, 2.0)

    print(f"Sleeping for {remaining_sleep} to keep traders in sync")
    time.sleep(max(0, remaining_sleep))
