"""
This is a config file for screen mirroring with an iPhone 15 Pro Max.
To use this with an iPhone 15 Pro Max, the only thing you should modify is the `anchor` variable.
"""

from Point import Point

# Red 'x' in the top left of the mirroring window
anchor = Point(3115, 695)  # 36" windscreen monitor
anchor = Point(1595, 335)  # 1080p monitor

# Individual offset values
start_battle_offset = Point(262, 590)
start_trade_offset = Point(112, 568)  # TODO: Update this since remote trades were added
first_trade_pokemon_offset = Point(46, 258)
between_first_second_pokemon_offset = Point(98, 252)  # unused
next_button_offset = Point(153, 626)
confirm_button_offset = Point(26, 391)
pokemon_details_left_health_white_offset = Point(31, 326)  # unused
x_button_offset = Point(153, 694)
start_drag_next_poke_offset = Point(281, 437)
end_drag_next_poke_offset = Point(32, 437)
modify_favorite_offset = Point(286, 75)
lets_do_it_offset = Point(150, 459)
great_league_offset = Point(157, 347)
ultra_league_offset = Point(157, 452)
master_league_offset = Point(157, 556)
lets_battle_offset = Point(150, 451)
first_pokemon_in_party_offset = Point(63, 547)
use_party_offset = Point(151, 664)
rematch_offset = Point(153, 479)
sort_button_offset = Point(273, 625)  # unused
first_pokemon_offset = Point(45, 331)
second_pokemon_offset = Point(152, 331)
third_pokemon_offset = Point(258, 331)
done_button_offset = Point(228, 707)

# Recreated configuration using anchor + individual offsets
coordinates = {
    "start_battle_coordinates": [
        anchor.x + start_battle_offset.x,
        anchor.y + start_battle_offset.y,
    ],
    "start_trade_coordinates": [
        anchor.x + start_trade_offset.x,
        anchor.y + start_trade_offset.y,
    ],
    "first_trade_pokemon_coordinates": [
        anchor.x + first_trade_pokemon_offset.x,
        anchor.y + first_trade_pokemon_offset.y,
    ],
    "between_first_second_pokemon": [
        anchor.x + between_first_second_pokemon_offset.x,
        anchor.y + between_first_second_pokemon_offset.y,
    ],
    "next_button_coordinates": [
        anchor.x + next_button_offset.x,
        anchor.y + next_button_offset.y,
    ],
    "confirm_button_coordinates": [
        anchor.x + confirm_button_offset.x,
        anchor.y + confirm_button_offset.y,
    ],
    "pokemon_details_left_health_white": [
        anchor.x + pokemon_details_left_health_white_offset.x,
        anchor.y + pokemon_details_left_health_white_offset.y,
    ],
    "x_button_coordinates": [anchor.x + x_button_offset.x, anchor.y + x_button_offset.y],
    "start_drag_next_poke": [
        anchor.x + start_drag_next_poke_offset.x,
        anchor.y + start_drag_next_poke_offset.y,
    ],
    "end_drag_next_poke": [
        anchor.x + end_drag_next_poke_offset.x,
        anchor.y + end_drag_next_poke_offset.y,
    ],
    "modify_favorite": [
        anchor.x + modify_favorite_offset.x,
        anchor.y + modify_favorite_offset.y,
    ],
    "lets_do_it_coordinates": [
        anchor.x + lets_do_it_offset.x,
        anchor.y + lets_do_it_offset.y,
    ],
    "great_league_coordinates": [
        anchor.x + great_league_offset.x,
        anchor.y + great_league_offset.y,
    ],
    "ultra_league_coordinates": [
        anchor.x + ultra_league_offset.x,
        anchor.y + ultra_league_offset.y,
    ],
    "master_league_coordinates": [
        anchor.x + master_league_offset.x,
        anchor.y + master_league_offset.y,
    ],
    "lets_battle_coordinates": [
        anchor.x + lets_battle_offset.x,
        anchor.y + lets_battle_offset.y,
    ],
    "first_pokemon_in_party_coordinates": [
        anchor.x + first_pokemon_in_party_offset.x,
        anchor.y + first_pokemon_in_party_offset.y,
    ],
    "use_party_coordinates": [
        anchor.x + use_party_offset.x,
        anchor.y + use_party_offset.y,
    ],
    "rematch_coordinates": [anchor.x + rematch_offset.x, anchor.y + rematch_offset.y],
    "sort_button_coordinates": [
        anchor.x + sort_button_offset.x,
        anchor.y + sort_button_offset.y,
    ],
    "first_pokemon_coordinates": [
        anchor.x + first_pokemon_offset.x,
        anchor.y + first_pokemon_offset.y,
    ],
    "second_pokemon_coordinates": [
        anchor.x + second_pokemon_offset.x,
        anchor.y + second_pokemon_offset.y,
    ],
    "third_pokemon_coordinates": [
        anchor.x + third_pokemon_offset.x,
        anchor.y + third_pokemon_offset.y,
    ],
    "done_button_coordinates": [
        anchor.x + done_button_offset.x,
        anchor.y + done_button_offset.y,
    ],
    "change_prng": False,
}
