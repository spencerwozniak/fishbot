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

![download](https://user-images.githubusercontent.com/98838077/210888907-0f02bc5f-25b1-46bd-af8d-870fa328c81e.png)

If we zoom in, we can see that the cyan pixel indicates the pixel that is being detected. 

![Screenshot 2023-01-05 170502](https://user-images.githubusercontent.com/98838077/210889033-4a74e0d5-3d81-428f-a631-1535be62d411.png)

This pixel is white (i.e. `RGB = (255,255,255)`) when the rod is casted and is not white when there is a fish caught. Therefore, we reel the rod in when the pixel is not white.
