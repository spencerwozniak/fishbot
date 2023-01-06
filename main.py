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

m.PAUSE = 0.1

def say(ctx, name='FishBot'):
    print(f'[{name}] {ctx}')

def cmd(txt):
    for char in txt:
        m.press(char)
    m.press('enter')

def sprint(time):
    keys = ('ctrl','w','space')
    for key in keys:
        m.keyDown(key)
    t.sleep(time)
    for key in keys:
        m.keyUp(key)

def turn(deg,dt=1.0,mx=6.75):
    if deg < 0:
        deg += 360
    m.PAUSE = dt/abs(deg)
    for i in range(deg): # 1.104 / deg
        m.moveRel((mx,0)) # 15 /degree
    m.PAUSE = 0.1

# Function that goes to shop and echest
def sell_fish(px=36, method='command'):
    
    def row_loop(x=9):
        m.PAUSE = 0.2
        for i in range(x):
            j = (8-i)*px
            m.click(button='right') # Select fish
            m.moveRel((j,0)) # Move to sell
            m.click(button='left') # Sell fish
            m.moveRel((-8*px,0)) # Move to return
            m.click(button='left') # Return to shop
            if i < x-1:
                m.moveRel((px*(i+1),0)) # Move to next fish
        m.PAUSE = 0.1
    
    if method != 'command':
        cmd('/fish') # Warp to fish shop

        say('Going to sell fish.')
        t.sleep(6)

        # Interact with fish merchant
        m.keyDown('w')
        t.sleep(0.3)
        say('Arrived at fishing merchant.')
        t.sleep(0.3)
        m.keyUp('w')
        m.click(button='right')
    else:
        cmd('/gshop')
        t.sleep(0.25)
        m.moveRel((px,-2.3*px))
        m.click(button='right')
        m.moveRel((-px,2.3*px))
    
    # Open Warzone fishing
    t.sleep(0.5)
    m.moveRel((0,-2.6*px))
    t.sleep(0.15)
    m.click(button='right')
    m.moveRel((-4*px,0))

    # Sell all fish
    row_loop(9)
    m.moveRel((0,px))
    row_loop(9)
    m.moveRel((6*px,-2*px))
    m.click(button='right')
    m.moveRel((-6*px,1.5*px))
    row_loop(9)
    m.moveRel((0,px))
    row_loop(6)
    say('All fish sold.')

    t.sleep(0.5)
    m.press('esc') # Exit fish shop
    

def go_fish():
    say('Going to fish.')
    # Warp to spawn and feed
    cmd('/spawn')
    cmd('/feed')
    t.sleep(10)

    # Go back to fishing spot
    m.keyDown('d')
    t.sleep(0.4)
    m.keyUp('d')
    sprint(12.0)
    turn(211)
    sprint(14.5)
    turn(84)
    sprint(40.0)
    turn(180)

    say('Arrived at fishing location.')

# Function for random mouse movement
def move_mouse(dt=1.0):
    x = r.random()*50+100
    y = r.random()*50+100

    m.moveRel(x,y,duration=dt/2) # Moves mouse away from original position
    m.moveRel(-x,-y,duration=dt/2) # Moves mouse back to original position

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
    keys = ('w','a','s','d')

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
    t.sleep(3*dt/4)
    m.press('esc')

    m.keyUp('shift')
    t.sleep(dt/4)
    m.keyDown('shift')


def fish(num_fish=50):
    n = 0

    m.keyDown('shift') # Sneak
    t.sleep(1.0) # 1 s delay

    m.PAUSE = 0.25
    m.press('2')
    m.press('1')
    m.PAUSE = 0.1

    while n < num_fish: # While script is running
        m.click(button='right') # Cast rod
        

        move_mouse(0.5) # Move mouse
        random_movement() # Move around randomly

        while True: # While rod is casted
            px = g.grab().load() # Looks at screen
            color = px[956,608] # Gets color of pixel

            if color != (255,255,255): # If pixel is not white
                say('Fish caught.')
                n += 1
                break # Leave fishing loop

        t.sleep(r.random()*0.1+0.2) # Random delay
        m.click(button='right') # Reel rod in
        
        #show_inventory(0.2) # Show inventory for 200 ms

    m.keyUp('shift')

def main():
    
    print('Open MC (Make sure rod is in hand)')
    t.sleep(5) # Gives 5 seconds to return to game
    
    m.press('f11') # Get out of fullscreen
    t.sleep(0.25) # Delay 250ms

    go_fish() # Go to fishing location

    while True:
        fish(num_fish=75)                    # Catch 75 fish
        sell_fish(px=36, method='command')   # Sell fish

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        t.sleep(0.05)
        m.keyUp('shift')
        t.sleep(0.05)
        sys.exit(0)
