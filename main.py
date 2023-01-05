#!/usr/bin/env python3

###############################
#                             #
# Fishing bot for MC factions #
#                             #
###############################

import sys
import pyautogui as m
import time as t
import random as r
from PIL import ImageGrab as g

# Function for mouse movement
def move_mouse(dt=0.2):
    m.moveRel(100,100,duration=dt/2) # Moves mouse away from original position
    m.moveRel(-100,-100,duration=dt/2) # Moves mouse back to original position

# Function for random character movement
def random_movement(a=0.05,b=0.1):
    keys = ['w','a','s','d']
    r.shuffle(keys) # Shuffles WASD key presses

    for key in keys:
        m.keyDown(key) # Key press
        t.sleep(r.random()*a + b) # Random delay
        
    for key in keys:
        m.keyUp(key) # Key release

# Function for fixed character movement
def fixed_movement(dt=0.05):
    keys = ['w','a','s','d']

    m.keyUp('shift')
    t.sleep(0.05)

    for key in keys:
        m.keyDown(key) # Key press
        t.sleep(dt)
        m.keyUp(key) # Key release

    t.sleep(0.05)
    m.keyDown('shift')

# Function that shows inventory
def show_inventory(dt=1.0):
    m.press('e')
    t.sleep(dt)
    m.press('esc')

    m.keyUp('shift')
    move_mouse(r.random()*0.05)
    m.keyDown('shift')

def main():

    print('Open MC at fishing location with rod in hand')
    t.sleep(5) # Gives 5 seconds to return to game
    
    m.press('f11') # Get out of fullscreen
    t.sleep(0.25) # Delay 250ms
    m.keyDown('shift') # Sneak

    while True: # While script is running
        m.click(button='right') # Cast rod

        fixed_movement(dt=0.33) # Move in a fixed pattern

        while True: # While rod is casted
            px = g.grab().load() # Looks at screen
            color = px[956,608] # Gets color of pixel

            if color != (255,255,255): # If pixel is not white
                print('Fish caught')
                break # Leave fishing loop

        t.sleep(r.random()*0.25) # Random delay
        m.click(button='right') # Reel rod in
        
        move_mouse(0.2) # Move mouse for 200 ms
        random_movement(a=0.02,b=0.02) # Move around randomly
        show_inventory(0.1) # Show inventory for 100 ms

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        t.sleep(0.05)
        m.keyUp('shift')
        t.sleep(0.05)
        sys.exit(0)
