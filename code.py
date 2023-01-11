#!/usr/bin/env python3

# Created By: Chris Di Bert
# Date: Jan. 11, 2023
# This prints "Hello, World!" to the screen

import stage
import ugame


def game_scene():
    # This function sets up and runs the main game scene.

    # Load the background and sprite image banks
    image_bank_background = stage.Bank.from_bmp16("space_aliens_background.bmp")
    image_bank_sprites = stage.Bank.from_bmp16("space_aliens.bmp")

    # Create the background grid using the image and set the size to 10x8 tiles
    background = stage.Grid(image_bank_background, 10, 8)

    # Create the ship sprite using image at index 5, with initial position
    # (72,57)
    ship = stage.Sprite(image_bank_sprites, 5, 72, 57)

    # Create a "Stage" object to manage the game graphics and input
    # Set the frame rate to 60fps
    game = stage.Stage(ugame.display, 60)

    # Add the background and ship to the layers list
    game.layers = [ship] + [background]

    # Draw the background on the screen
    game.render_block()

    # Repeats forever
    while True:
        pass


if __name__ == "__main__":
    game_scene()
