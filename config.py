# Define the active system
ACTIVE_SYSTEM = "iPhone15ProMaxWidescreen"

# TODO: Scale these based on Ex. top left and bottom right corners or something
#       Scale would be dependent on screen aspect ratio
# Define system-specific coordinates
#   Depending on which script you are running,
#   not all of these need to be defined
systems = {
    "iPhone15ProMaxWidescreen": {  # Widescreen monitor
        "start_battle_coordinates": [3377, 1285],
        "start_trade_coordinates": [3283, 1285],
        "first_trade_pokemon_coordinates": [3161, 953],
        # "between_first_second_pokemon": [3213, 947],  # Whitespace
        "next_button_coordinates": [3268, 1321],
        "confirm_button_coordinates": [3141, 1086],
        # "pokemon_details_left_health_white": [3146, 1021],  # Whitespace left of health bar
        "x_button_coordinates": [3268, 1389],
        "start_drag_next_poke": [3396, 1132],  # Right side of screen
        "end_drag_next_poke": [3147, 1132],  # Left side of screen
        "modify_favorite": [3401, 770],
        "lets_do_it_coordinates": [3265, 1154],
        "great_league_coordinates": [3272, 1042],
        "ultra_league_coordinates": [3272, 1147],
        "master_league_coordinates": [3272, 1251],
        "lets_battle_coordinates": [3265, 1146],
        "first_pokemon_in_party_coordinates": [3178, 1242],
        "use_party_coordinates": [3266, 1359],
        "rematch_coordinates": [3268, 1174],
        # "sort_button_coordinates": [3388,1320],   # Unused
        "first_pokemon_coordinates": [3160, 1026],
        "second_pokemon_coordinates": [3267, 1026],
        "third_pokemon_coordinates": [3373, 1026],
        "done_button_coordinates": [3343, 1402],
        "change_prng": False,  # One of the devices should be false, the other true. This allows their 'randomness' to be different
    },
    "iPhone11ProMBAirLarger": {  # iPhone Mirroring -> View -> Larger
        "start_battle_coordinates": [1608, 871],
        "start_trade_coordinates": [1493, 871],
        "first_trade_pokemon_coordinates": [1366, 489],
        # "between_first_second_pokemon": [1420, 488],  # Unused
        "next_button_coordinates": [1487, 917],
        "confirm_button_coordinates": [1347, 650],
        # "pokemon_details_left_health_white": [1350, 579], # Unused
        "x_button_coordinates": [1486, 995],
        "start_drag_next_poke": [1633, 710],
        "end_drag_next_poke": [1340, 710],
        "modify_favorite": [1636, 294],
        "lets_do_it_coordinates": [1483, 728],
        "great_league_coordinates": [1485, 604],
        "ultra_league_coordinates": [1486, 720],
        "master_league_coordinates": [1487, 841],
        "lets_battle_coordinates": [1482, 719],
        "first_pokemon_in_party_coordinates": [1384, 828],
        "use_party_coordinates": [1499, 959],
        "rematch_coordinates": [1482, 750],
        # "sort_button_coordinates": [1621, 915],   # Unused
        "first_pokemon_coordinates": [1367, 566],
        "second_pokemon_coordinates": [1485, 566],
        "third_pokemon_coordinates": [1602, 566],
        "done_button_coordinates": [1571, 1009],
        "change_prng": True,
    },
}

# Get the active system's coordinates
SETTINGS = systems[ACTIVE_SYSTEM]
