#!/usr/bin/env python3

import os
import sys
import pyautogui as m
import time as t
from PIL import ImageGrab as g

def zoom_in(img, x, y, zoom=10):
    w, h = img.size
    zoom2 = zoom * 2
    img = img.crop((x - w / zoom2, y - h / zoom2, 
                    x + w / zoom2, y + h / zoom2))
    return img

def main():

    print('Open MC at fishing location with rod in hand')
    t.sleep(5) # Gives 5 seconds to return to game
    
    m.press('f11') # Get out of fullscreen
    t.sleep(0.1) # Delay 100ms
    m.click(button='right')
    t.sleep(0.1) # Delay 100ms

    im_orig = g.grab() # Takes screenshot
    im_orig.format = "PNG"

    m.press('esc')
    
    good = False

    while not good:
        im = im_orig.copy()

        try:
            x = int(input('x: '))
            y = int(input('y: '))
        except ValueError:
            print('[Error] XY coordinates must be an integer')
            continue

        im.putpixel((x,y), (0, 255, 255))
        zoom_in(im, x, y).show()
        
        while True:
            ask = input('good? (y/n) ')
            if ask.upper() == 'N':
                break
            elif ask.upper() == 'Y':
                good = True
                break
            else:
                print('[Error] Please enter (y/n)')


    script = os.path.join(os.path.dirname(os.path.realpath(sys.argv[0])), 'main.py')

    with open(script, 'r') as f:
        fdata = f.readlines()

    fdata[70] = f'            color = px[{x},{y}] # Gets color of pixel\n'
        
    with open(script, 'w') as f:
        f.writelines(fdata)

    print("Successfully modified 'main.py'")
    t.sleep(3)
    sys.exit(0) 

if __name__ == '__main__':
    main()
