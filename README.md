# PokemonGoMirrorBot
PokemonGo Bot via screen mirroring

### About
Using [screen mirroring](https://support.apple.com/en-us/120421), click on repeatable locations with random delays and random click accuracy.

### Configuration
Edit the coordinates for your system in [`config.py`](config.py). I'd recommend placing the screen mirroring application in an easily repeatable location (Ex. bottom right of screen).

The coordinates of the current mouse position can be easily obtained via `cmd` + `shift` + `4`.

Some of the scripts use `Cliclick.get_color()`, which takes a screenshot, to make sure the scripts are on the expected screen. Disable the "Catch Card" notification as this notification can cause some scripts to fail.
* Pokeball (bottom center) --> Settings (top right) --> Notifications --> In-Game Notifications --> Catch Card --> Off

The easiest way to find out the color at a certain location is by using macOS's built in "Digital Color Meter.app".

### Dependencies
* Python
* [cliclick](https://github.com/BlueM/cliclick)

### Supported bot actions
* Trading
