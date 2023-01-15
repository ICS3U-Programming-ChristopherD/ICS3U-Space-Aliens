#!/usr/bin/env python3
 
# Created By: Chris Di Bert
# Date: Jan. 11, 2023
# This is the "Alien Annihilator" game for the PyBadge


import stage
import ugame

import constants

def menu_scene():

    # Load the background and sprite image banks
    image_bank_background = stage.Bank.from_bmp16("space_aliens_background.bmp")


    # add text objects
    text = []
    text1 = stage.Text(width=29, height=12, font=None, palette=constants.RED_PALETTE, buffer=None) 
    text1.move(20, 10)
    text1.text("DVD Project Blue")
    text.append(text1)

    text2 = stage.Text(width=29, height=12, font=None, palette=constants.RED_PALETTE, buffer=None) 
    text2.move(40, 110)
    text2.text("PRESS START")
    text.append(text2)

    # Create the background grid using the image and set the size to 10x8 tiles
    background = stage.Grid(image_bank_background, constants.SCREEN_GRID_X, constants.SCREEN_GRID_Y)

    # Create a "Stage" object to manage the game graphics and input
    # Set the frame rate to 60fps
    game = stage.Stage(ugame.display, constants.FP5)

    # Add the background and ship to the layers list
    game.layers = text + [background]

    # Draw the background on the screen
    game.render_block()

    # Repeat forever
    while True:
        # Gets user input
        keys = ugame.buttons.get_pressed()

        if keys & ugame.K_START != 0:
            game_scene()

        # Redraw sprites
        game.tick()

def game_scene():

    # Load the background and sprite image banks
    image_bank_background = stage.Bank.from_bmp16("space_aliens_background.bmp")
    image_bank_sprites = stage.Bank.from_bmp16("space_aliens.bmp")

    # Buttons to keep state information on
    a_button = constants.button_state["button_up"]
    b_button = constants.button_state["button_up"]
    start_button = constants.button_state["button_up"]
    select_button = constants.button_state["button_up"]

    # Get sound ready
    pew_sound = open("pew.wav", "rb")
    sound = ugame.audio
    sound.stop()
    sound.mute(False)


    # Create the background grid using the image and set the size to 10x8 tiles
    background = stage.Grid(image_bank_background, constants.SCREEN_GRID_X, constants.SCREEN_GRID_Y)

    # Initializes the alien variable to a sprite from image bank sprites and gets the fifth image
    ship = stage.Sprite(image_bank_sprites, 1, 75, constants.SCREEN_Y - (2*constants.SPRITE_SIZE))

    # Initializes the ship variable to a sprite from image bank sprites and gets the seventh image
    alien = stage.Sprite(image_bank_sprites, 7, int(constants.SCREEN_X / 2 - constants.SPRITE_SIZE / 2), 16)

    # Create a "Stage" object to manage the game graphics and input
    # Set the frame rate to 60fps
    game = stage.Stage(ugame.display, constants.FP5)

    # Add the background and ship to the layers list
    game.layers = [ship] + [alien] + [background]

    # Draw the background on the screen
    game.render_block()

    # Repeat forever
    while True:
        # Gets user input
        keys = ugame.buttons.get_pressed()


        # A button to fire
        if keys & ugame.K_O != 0:
            if a_button == constants.button_state["button_up"]:
                a_button = constants.button_state["button_just_pressed"]
            elif a_button == constants.button_state["button_just_pressed"]:
                a_button = constants.button_state["button_still_pressed"]
            else:
                if a_button == constants.button_state["button_still_pressed"]:
                    a_button = constants.button_state["button_released"]
                else:
                    a_button = constants.button_state["button_up"]


        if keys & ugame.K_X != 0:
            pass
        if keys & ugame.K_START != 0:
            pass
        if keys & ugame.K_SELECT != 0:
            pass

        if keys & ugame.K_RIGHT != 0:
            if ship.x <= constants.SCREEN_X - constants.SPRITE_SIZE:
                ship.move(ship.x + constants.SPRITE_MOVEMENT_SPEED, ship.y)
            else:
                ship.move(constants.SCREEN_X - constants.SPRITE_SIZE, ship.y)    

        if keys & ugame.K_LEFT != 0:
            if ship.x >= 0:
                ship.move(ship.x - constants.SPRITE_MOVEMENT_SPEED, ship.y)
            else:
                ship.move(0,ship.y)

        if keys & ugame.K_UP != 0:
            # ship.move(ship.x, ship.y - 1)
            pass         
        if keys & ugame.K_DOWN != 0:
            # ship.move(ship.x, ship.y + 1)
            pass

        # Play sound if A was just button_just_pressed
        if a_button == constants.button_state["button_just_pressed"]:
            sound.play(pew_sound)

        # Redraw sprites
        game.render_sprites([ship] + [alien])
        game.tick()


if __name__ == "__main__":
    menu_scene()
