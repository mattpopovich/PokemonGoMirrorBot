# Define the active system
ACTIVE_SYSTEM = "iPhone15ProMaxWidescreen"

# Define system-specific coordinates
#   Depending on which script you are running,
#   not all of these need to be defined
systems = {
    "iPhone15ProMaxWidescreen": {
        "start_trade_coordinates": [3377, 1285],
        "first_pokemon_coordinates": [3161, 953],
        "next_button_coordinates": [3268, 1321],
        "confirm_button_coordinates": [3141, 1086],
        "x_button_coordinates": [3268, 1389],
        "start_drag_next_poke": [3396, 1132],   # Right side of screen
        "end_drag_next_poke": [3147, 1132],     # Left side of screen
        "modify_favorite": [3401, 770],
        "first_pokemon_health_coordinates": [3146,980],
        "change_delay": False
    },
    "iPhone11ProMBAirLarger": {
        "start_trade_coordinates": [1608, 871],
        "first_pokemon_coordinates": [1366, 489],
        "next_button_coordinates": [1487, 917],
        "confirm_button_coordinates": [1347, 650],
        "x_button_coordinates": [1486, 995],
        "change_delay": True
    },
}

# Get the active system's coordinates
SETTINGS = systems[ACTIVE_SYSTEM]
