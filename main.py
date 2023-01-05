#!/usr/bin/env python3
#
# Fishing bot for MC factions
#

import pyautogui as m
from PIL import Image, ImageGrab
import time as t

def main():
    
    print('Open MC at fishing location with rod in hand')
    t.sleep(10) # Gives 10 seconds to return to game

    # Main loop
    while True:
        #m.click(button='right') # Cast rod
        
        # Fishing loop
        while True:
            px = ImageGrab.grab().load() # Looks at screen
            color = px[960,600] # Gets color of pixel
            print(color)

            if color == True: # If color is ''
                print('Fish caught')
                break # Leave fishing loop

        #m.click(button='right') # Reel rod in
        t.sleep(0.1) # Delay 100ms before casting

if __name__ == '__main__':
    main()
