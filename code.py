#!/usr/bin/env python3
 
# Created By: Chris Di Bert
# Date: Jan. 11, 2023
# This is the "Alien Annihilator" game for the PyBadge


import stage
import ugame

import constants

def game_scene():

    # Load the background and sprite image banks
    image_bank_background = stage.Bank.from_bmp16("space_aliens_background.bmp")
    image_bank_sprites = stage.Bank.from_bmp16("space_aliens.bmp")

    # Create the background grid using the image and set the size to 10x8 tiles
    background = stage.Grid(image_bank_background, constants.SCREEN_GRID_X, constants.SCREEN_GRID_Y)

    # Initializes the ship variable to a sprite from image bank sprites and gets the fifth image and sets x = 75 y= 66
    ship = stage.Sprite(image_bank_sprites, 1, 75, constants.SCREEN_Y - (2*constants.SPRITE_SIZE))

    # Create a "Stage" object to manage the game graphics and input
    # Set the frame rate to 60fps
    game = stage.Stage(ugame.display, constants.FP5)

    # Add the background and ship to the layers list
    game.layers = [ship] + [background]

    # Draw the background on the screen
    game.render_block()

    # Repeat forever
    while True:
        # Gets user input
        keys = ugame.buttons.get_pressed()

        if keys & ugame.K_X:
            pass
        if keys & ugame.K_O:
            pass
        if keys & ugame.K_START:
            pass
        if keys & ugame.K_SELECT:
            pass
        if keys & ugame.K_RIGHT:
            if ship.x <= constants.SCREEN_X - constants.SPRITE_SIZE:
                ship.move(ship.x + constants.SPRITE_MOVEMENT_SPEED, ship.y)
            else:
                ship.move(constants.SCREEN_X - constants.SPRITE_SIZE, ship.y)    

        if keys & ugame.K_LEFT:
            if ship.x >= 0:
                ship.move(ship.x - constants.SPRITE_MOVEMENT_SPEED, ship.y)
            else:
                ship.move(0,ship.y)

        if keys & ugame.K_UP:
            # ship.move(ship.x, ship.y - 1)
            pass         
        if keys & ugame.K_DOWN:
            # ship.move(ship.x, ship.y + 1)
            pass

        # Redraw sprites
        game.render_sprites([ship])
        game.tick()

if __name__ == "__main__":
    game_scene()
