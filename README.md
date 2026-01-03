# PokemonGoMirrorBot
PokemonGo Bot via screen mirroring

### About
Using iPhone/Mac [screen mirroring](https://support.apple.com/en-us/120421), click on repeatable locations with random delays and random click accuracy in order to automate repetitive PokemonGo Tasks.

### Configuration
Edit the `anchor` point for your system in one of the `.yaml` files in [`configs/`](/configs). I'd recommend placing the screen mirroring application in an easily repeatable location (Ex. bottom right of screen). The anchor point should be the center of the red 'x' on the top left of the screen mirroring window.

The coordinates of the current mouse position can be easily obtained via `cmd` + `shift` + `4`.
<!--
Some of the scripts use `Cliclick.get_color()`, which takes a screenshot, to make sure the scripts are on the expected screen. Disable the "Catch Card" notification as this notification can cause some scripts to fail.
* Pokeball (bottom center) -> Settings (top right) -> Notifications -> In-Game Notifications -> Catch Card -> Off

The easiest way to find out the color at a certain location is by using macOS's built in "Digital Color Meter.app".
-->

### Dependencies
* Python
* [cliclick](https://github.com/BlueM/cliclick) ([`brew install cliclick`](https://formulae.brew.sh/formula/cliclick))
* [pyyaml](https://pypi.org/project/PyYAML/)
  * ```shell
    python3 -m venv myenv
    source myenv/bin/activate
    pip3 install pyyaml
    ```

### Examples
* `CONFIG=iPhone11.yaml python3 trader.py`
* `CONFIG=iPhoneMax.yaml python3 modifyFavorite.py`
* `python3 battler.py --master --lose` and `python3 battler.py --win`

### Supported bot actions
* Trading
* Modifying the favorite status of Pokemon
* Battling against another account

### Helpful search strings
* See all pokemon that can evolve with 0 candy
  * `64,67,75,93,525,533,588,616,708,710&traded`
* See all pokemon that were caught within 1km of your current location (1 trade candy)
  * `distance1`
* See all pokemon that were caught within 11-99km of your current location (2 trade candies)
  * `distance11-&distance99`
* See all pokemon that were caught further than 101km away (3 trade candies)
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
