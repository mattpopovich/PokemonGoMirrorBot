# PokemonGoMirrorBot
PokemonGo Bot via screen mirroring

### About
Using [screen mirroring](https://support.apple.com/en-us/120421), click on repeatable locations with random delays and random click accuracy.

### Configuration
Edit the coordinates for your system in [`config.py`](config.py). I'd recommend placing the screen mirroring application in an easily repeatable location (Ex. bottom right of screen).

The coordinates of the current mouse position can be easily obtained via `cmd` + `shift` + `4`.
<!--
Some of the scripts use `Cliclick.get_color()`, which takes a screenshot, to make sure the scripts are on the expected screen. Disable the "Catch Card" notification as this notification can cause some scripts to fail.
* Pokeball (bottom center) -> Settings (top right) -> Notifications -> In-Game Notifications -> Catch Card -> Off

The easiest way to find out the color at a certain location is by using macOS's built in "Digital Color Meter.app".
-->

### Dependencies
* Python
* [cliclick](https://github.com/BlueM/cliclick)

### Supported bot actions
* Trading
* Modifying the favorite status of Pokemon
* Battling against another account

### Helpful search strings
* See all pokemon that can evolve with 0 candy
  * `64,67,75,93,525,533,588,616,708,710&traded`
* See all pokemon that were caught within 1km of your current location
  * `distance1`
* See all pokemon that were caught within 11-99km of your current location
  * `distance11-&distance99`
* See all pokemon that were caught further than 101km away
  * `distance101-`

### My routine
* First, I check for nundos with the search string `0attack&0defense&0hp` and favorite them
* Second, I search to see which pokemon I can evolve with 0 candy and I will either evolve them or save them for evolution later (just make sure that I evolve them before transferring)
* Then, I will go through recently acquired pokemon and "favorite" any that are strong
* Next, I apply a tag named "transfer" to all the pokemon that I am okay with transferring away
  * `!@special&!lucky&!legendary&!mythical&!costume&!ultra beasts&!shiny&!xxl&!xxs&!candyxl&!locationbackground&!specialbackground&!favorite&!shadow&!purified&!dynamax&!4*&!3*&!futureTransfer`
    * `futureTransfer` = Pokemon that I don't want but are too good to throw away. I'll save them for whenever there is an enhanced lucky transfer rate.
* Finally, I will trade any pokemon with the "transfer" tag to a friend
  * Use the distance search string above to your advantage to maximize 100+km transfers and 10+km transfers.
  * Any pokemon that matches `transfer&traded` can be transferred to the professor. I will transfer them all to the professor whenever there is an enhanced transfer candy rate.
* Lastly, I will go through my pokemon list and unfavorite any Pokemon that I thought were strong but I actually have stronger versions of.
  * I try to keep 6 of every Pokemon but I understand that is somewhat crazy... 😬
