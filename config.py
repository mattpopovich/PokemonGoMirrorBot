# Define the active system
ACTIVE_SYSTEM = "iPhone15ProMaxWidescreen"

# Define system-specific coordinates
#   Depending on which script you are running,
#   not all of these need to be defined
systems = {
    "iPhone15ProMaxWidescreen": {               # Widescreen monitor
        "start_battle_coordinates": [3377, 1285],
        "start_trade_coordinates": [3283, 1285],
        "first_pokemon_coordinates": [3161, 953],
        "between_first_second_pokemon": [3213, 947],    # Whitespace
        "next_button_coordinates": [3268, 1321],
        "confirm_button_coordinates": [3141, 1086],
        "pokemon_details_left_health_white": [3146, 1021],  # Whitespace left of the health bar
        "x_button_coordinates": [3268, 1389],
        "start_drag_next_poke": [3396, 1132],   # Right side of screen
        "end_drag_next_poke": [3147, 1132],     # Left side of screen
        "modify_favorite": [3401, 770],
        "change_delay": False
    },
    "iPhone11ProMBAirLarger": {                 # iPhone Mirroring -> View -> Larger
        "start_battle_coordinates": [1608, 871],
        "start_trade_coordinates": [1493, 871],
        "first_pokemon_coordinates": [1366, 489],
        "between_first_second_pokemon": [1420, 488],
        "next_button_coordinates": [1487, 917],
        "confirm_button_coordinates": [1347, 650],
        "pokemon_details_left_health_white": [1350, 579],
        "x_button_coordinates": [1486, 995],
        "start_drag_next_poke": [1633, 710],
        "end_drag_next_poke": [1340, 710],
        "modify_favorite": [1636,294],
        "change_delay": True
    },
}

# Get the active system's coordinates
SETTINGS = systems[ACTIVE_SYSTEM]
