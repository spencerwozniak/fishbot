# FishBot

### Features
- Casts rod and reels rod in when fish is caught (v1)
- Avoids AFK kick by moving character and mouse position (v2)

### First time setup
- Make sure Python 3.x is installed
- Run install.bat

### To use
- Go to fishing location
- Pull out rod
- Run main.py
- Go back to game

### To stop
- Hit ESC in game
- Go to CMD and hit CTRL+C

## How it works
This script works by detecting color changes of a pixel that is specific to fishing. The loop for fishing is shown in the code below.
```
while True: # While rod is casted
    px = g.grab().load() # Looks at screen
    color = px[956,608] # Gets color of pixel at position x=956, y=608

    if color != (255,255,255): # If pixel is not white
        print('Fish caught')
        break # Leave fishing loop
```
This is what the window should look like when the script is running properly:

<img src="images/orignal.png" alt="original" width="200"/>

If we zoom in, we can see that the cyan pixel indicates the pixel that is being detected. 

<img src="images/pixel.png" alt="original" width="200"/>

This pixel is white (`RGB == (255,255,255)`) when the rod is casted and is not white (`RGB != (255,255,255)`) when there is a fish caught. Therefore, we reel the rod in when the pixel is not white.
