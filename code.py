#!/usr/bin/env python3
 
# Created By: Chris Di Bert
# Date: Jan. 11, 2023
# This prints "Hello, World!" to the screen
 
import ugame
import stage
 
 
def game_scene():
 
# Image banks for CircuitPython
    image_bank_background = stage.Bank.from_bmp16("space_aliens_background.bmp")
# Sets the background image to image 0 in the image bank and the size (10x8 tiles of size 16x16)
    background = stage.Grid(image_bank_background, 10, 8)
 
# Create a stage for the background to show up on and set
# the frame rate to 60fps
    game = stage.Stage(ugame.display, 60)
 
# Set the layers, items show up in order
    game.layers = [background]
 
# Render the background and sprites
    game.render_block()
 
    # Repeats forever
    while True:
        pass
 
 
if __name__ == "__main__":
    game_scene()
