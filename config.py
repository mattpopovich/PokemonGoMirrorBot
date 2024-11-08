# Define the active system
ACTIVE_SYSTEM = "iPhone15ProMaxWidescreen"

# Define system-specific coordinates
systems = {
    "iPhone15ProMaxWidescreen": {
        "startTrade": [3377, 1285],
        "bottomCenterPokemon": [3266, 1321],
        "next_button": [3268, 1321],
        "confirm": [3141, 1086],
        "x": [3268, 1389],
    },
    "iphone11ProMBAirLarger": {
        "startTrade": [1608, 871],
        "bottomCenterPokemon": [1486, 893],
        "next_button": [1487, 917],
        "confirm": [1347, 650],
        "x": [1486, 995],
    },
}

# Get the active system's coordinates
ACTIVE_COORDINATES = systems[ACTIVE_SYSTEM]
