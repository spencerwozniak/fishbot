#!/usr/bin/env python3

import os
import sys
import pyautogui as m
import time as t
from PIL import ImageGrab as g

# Function for zooming in on a specific pixel
# https://stackoverflow.com/questions/46149003/pil-zoom-into-image-at-a-particular-point
def zoom_in(img, x, y, zoom=10):
    w, h = img.size
    zoom2 = zoom * 2
    img = img.crop((x - w / zoom2, y - h / zoom2, 
                    x + w / zoom2, y + h / zoom2))
    return img

def simulate_bot_loadup():
    print('Open MC at fishing location with rod in hand')
    t.sleep(5) # Gives 5 seconds to return to game
    m.press('f11') # Get out of fullscreen
    t.sleep(0.25) # Delay 100ms
    m.click(button='right')
    t.sleep(0.1) # Delay 100ms
    
    
def main():

    simulate_bot_loadup() # Simulates bot loading up

    im_orig = g.grab() # Takes screenshot
    im_orig.format = "PNG" # Changes format from BMP to PNG

    m.press('esc') # Pause game
    
    good = False # Pixel position is NOT good yet

    while not good:
        im = im_orig.copy() # Copies original screenshot to new Image object

        try:
            x = int(input('x: ')) # Input x coordinate
            y = int(input('y: ')) # Input y coordinate
        except ValueError:
            # Handles non integer inputs
            print('[Error] XY coordinates must be an integer')
            continue # Back to start of while loop

        im.putpixel((x,y), (0, 255, 255)) # Changes color of pixel at position (x,y) to cyan
        zoom_in(im, x, y).show() # Displays zoomed in image with pixel color change
        
        while True:
            ask = input('good? (y/n) ') # Asks whether the input pixel position is good
            if ask.upper() == 'N':
                break # Leave this while loop
            elif ask.upper() == 'Y':
                good = True # Pixel position is good
                break # Leave this while loop
            else:
                print('[Error] Please enter (y/n)')


    script = os.path.join(os.path.dirname(os.path.realpath(sys.argv[0])), 'main.py') # Gets path to main.py

    # Reads main.py into memory
    with open(script, 'r') as f:
        fdata = f.readlines()

    # Updates line 71 with new pixel position
    fdata[70] = f'            color = px[{x},{y}] # Gets color of pixel\n'
    
    # Writes fdata to main.py
    with open(script, 'w') as f:
        f.writelines(fdata)

    print("Successfully modified 'main.py'")
    t.sleep(3)
    sys.exit(0) 

if __name__ == '__main__':
    main()
