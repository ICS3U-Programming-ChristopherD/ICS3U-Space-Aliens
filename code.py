#!/usr/bin/env python3

# Created By: Chris Di Bert
# Date: Jan. 11, 2023
# This prints "Hello, World!" to the screen

import ugame
import stage


def game_scene():

    image_bank_background = stage.Bank.from_bmp16("space_aliens_background.bmp")
    background = stage.Grid(image_bank_background, 10, 8)

    game = stage.Stage(ugame.display, 60)
    game.layers = [background]
    game.render_block()

    # Repeats forever
    while True:
        pass


if __name__ == "__main__":
    game_scene()
