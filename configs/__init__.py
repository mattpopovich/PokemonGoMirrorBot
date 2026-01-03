import yaml
import os
from pathlib import Path

# Default config file name if none is specified
DEFAULT_CONFIG_NAME = "iPhoneMax.yaml"

# The directory containing the config files (this package's directory)
CONFIG_DIR = Path(__file__).parent


def load_config(config_name: str | None = None) -> dict:
    """
    Load a config YAML file and return the computed coordinates dictionary.

    Args:
        config_name: Name of the YAML file (without path).
                     If None, uses CONFIG environment variable
                     If no CONFIG environment variable, uses DEFAULT_CONFIG_NAME

    Returns:
        Dictionary of coordinates with the anchor added to them
    """
    if config_name is None:
        config_name = os.getenv("CONFIG")
        if config_name is None:
            print(
                f"No CONFIG environment variable set, using the default of CONFIG={DEFAULT_CONFIG_NAME}"
            )
            config_name = DEFAULT_CONFIG_NAME

    config_path = CONFIG_DIR / config_name

    if not config_path.exists():
        raise FileNotFoundError(f"Config file not found: {config_name}")

    with open(config_path, "r") as f:
        config = yaml.safe_load(f)

    anchor_x = config["anchor"]["x"]
    anchor_y = config["anchor"]["y"]
    offsets = config["offsets"]

    def get_coordinate_plus_anchor(offset_key: str) -> list[int]:
        """
        Get coordinates of offset_key, add the anchor, and return
        """
        offset = offsets[offset_key]
        return [anchor_x + offset["x"], anchor_y + offset["y"]]

    # coordinate key : yaml key
    key_mapping = {
        "start_battle_coordinates": "start_battle",
        "start_trade_coordinates": "start_trade",
        "first_trade_pokemon_coordinates": "first_trade_pokemon",
        "between_first_second_pokemon": "between_first_second_pokemon",
        "next_button_coordinates": "next_button",
        "confirm_button_coordinates": "confirm_button",
        "pokemon_details_left_health_white": "pokemon_details_left_health_white",
        "x_button_coordinates": "x_button",
        "start_drag_next_poke": "start_drag_next_poke",
        "end_drag_next_poke": "end_drag_next_poke",
        "modify_favorite": "modify_favorite",
        "lets_do_it_coordinates": "lets_do_it",
        "great_league_coordinates": "great_league",
        "ultra_league_coordinates": "ultra_league",
        "master_league_coordinates": "master_league",
        "lets_battle_coordinates": "lets_battle",
        "first_pokemon_in_party_coordinates": "first_pokemon_in_party",
        "use_party_coordinates": "use_party",
        "rematch_coordinates": "rematch",
        "sort_button_coordinates": "sort_button",
        "first_pokemon_coordinates": "first_pokemon",
        "second_pokemon_coordinates": "second_pokemon",
        "third_pokemon_coordinates": "third_pokemon",
        "done_button_coordinates": "done_button",
    }

    coordinates = {
        coordinate_key: get_coordinate_plus_anchor(yaml_key)
        for coordinate_key, yaml_key in key_mapping.items()
    }

    # Add everything else from the YAML that is NOT 'anchor' or 'offsets'
    for key, value in config.items():
        if key not in {"anchor", "offsets"}:
            coordinates[key] = value

    return coordinates


# Load config
coordinates = load_config()
