"""
This is a config file for screen mirroring with an iPhone 11 with a "Larger" view window.
To use this with an iPhone 11, the only thing you should modify is the `anchor` variable.
"""

from Point import Point

# Red 'x' in the top left of the mirroring window
anchor = Point(1311, 213)  # MacBook Air

# Individual offset values with a "larger" view
#   iPhone Mirroring -> View -> Larger
start_battle_offset = Point(286, 633)
start_trade_offset = Point(129, 636)
first_trade_pokemon_offset = Point(55, 276)
between_first_second_pokemon_offset = Point(109, 275)  # unused
next_button_offset = Point(176, 704)
confirm_button_offset = Point(36, 437)
pokemon_details_left_health_white_offset = Point(39, 366)  # unused
x_button_offset = Point(175, 782)
start_drag_next_poke_offset = Point(322, 497)
end_drag_next_poke_offset = Point(29, 497)
modify_favorite_offset = Point(325, 81)
lets_do_it_offset = Point(172, 515)
great_league_offset = Point(174, 391)
ultra_league_offset = Point(175, 507)
master_league_offset = Point(176, 628)
lets_battle_offset = Point(171, 506)
first_pokemon_in_party_offset = Point(73, 615)
use_party_offset = Point(188, 746)
rematch_offset = Point(171, 537)
sort_button_offset = Point(310, 702)  # unused
first_pokemon_offset = Point(56, 353)
second_pokemon_offset = Point(174, 353)
third_pokemon_offset = Point(291, 353)
done_button_offset = Point(260, 796)

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
    "change_prng": True,
}
