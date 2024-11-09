# Define the active system
ACTIVE_SYSTEM = "iPhone15ProMaxWidescreen"

# Define system-specific coordinates
systems = {
    "iPhone15ProMaxWidescreen": {
        "start_trade_coordinates": [3377, 1285],
        "first_pokemon_coordinates": [3161, 953],
        "next_button_coordinates": [3268, 1321],
        "confirm_button_coordinates": [3141, 1086],
        "x_button_coordinates": [3268, 1389],
        "change_delay": False
    },
    "iphone11ProMBAirLarger": {
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
