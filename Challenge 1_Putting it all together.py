### The following code section is used to set up connection with the sense-hat ###

from sense_hat import SenseHat
from time import sleep
from random import choice         # If you want to choose a random item from a list, use the choice function

sense = SenseHat()        # Create a sensehat object

### Define variables for the required colours (white, green, red, blank)

w = (150, 150, 150)        # white
bl = (0, 0, 0)                     # blank
g = (0, 255, 0)                 # green
r = (255, 0, 0)                  # red

### Create 3 different arrows (white, green, red)

arrow_w = [    bl, bl, bl, w, w, bl, bl, bl,
                        bl, bl, w, w, w, w, bl, bl,
                        bl, w, bl, w, w, bl, w, bl,
                        w, bl, bl, w, w, bl, bl, w,
                        bl, bl, bl, w, w, bl, bl, bl,
                        bl, bl, bl, w, w, bl, bl, bl,
                        bl, bl, bl, w, w, bl, bl, bl,
                        bl, bl, bl, w, w, bl, bl, bl
               ]

arrow_r = [    bl, bl, bl, r, r, bl, bl, bl,
                        bl, bl, r, r, r, r, bl, bl,
                        bl, r, bl, r, r, bl, r, bl,
                        r, bl, bl, r, r, bl, bl, r,
                        bl, bl, bl, r, r, bl, bl, bl,
                        bl, bl, bl, r, r, bl, bl, bl,
                        bl, bl, bl, r, r, bl, bl, bl,
                        bl, bl, bl, r, r, bl, bl, bl
               ]
                        
arrow_g = [    bl, bl, bl, g, g, bl, bl, bl,
                        bl, bl, g, g, g, g, bl, bl,
                        bl, g, bl, g, g, bl, g, bl,
                        g, bl, bl, g, g, bl, bl, g,
                        bl, bl, bl, g, g, bl, bl, bl,
                        bl, bl, bl, g, g, bl, bl, bl,
                        bl, bl, bl, g, g, bl, bl, bl,
                        bl, bl, bl, g, g, bl, bl, bl
               ]
pause = 2.0    # Set a variable pause to 3 (the initial time between turns)
score = 0        # Set a variable score to 0
angle = 0        # Set a variable angle to 0

### Set a variable called play to True (this will be used to stop the game later)

play = True

sense.show_message("Keep the arrow pointing up", scroll_speed = 0.05, text_colour = [100, 100, 100])


while play:
    
    # Choose a new random angle
    prev_angle = angle
    while angle == prev_angle:
        angle = choice([0, 90, 180, 270])
        
    sense.set_rotation(angle)
    
    # Display the white arrow
    sense.set_pixels(arrow_w)
    
    # Sleep for current pause length
    sleep(pause)
    
    acceleration = sense.get_accelerometer_raw()
    
    x = acceleration['x']
    y = acceleration['y']
    z = acceleration['z']
    
    x = round(x, 0)
    y = round(y, 0)
    z = round(z, 0)
    
    print(angle)
    print(x)
    print(y)
    
    # If the orientation matches the arrow,  add a point and turn the arrow green
    
    if x == -1 and angle == 180:
        
        sense.set_pixels(arrow_g)
        score += 1
        
    elif x ==1 and angle == 0:
        sense.set_pixels(arrow_g)
        score +=1

    elif y == -1 and angle == 90:
        sense.set_pixels(arrow_g)
        score += 1

    elif y == 1 and angle == 270:
        sense.set_pixels(arrow_g)
        score +=1

    else:
        sense.set_pixels(arrow_r)
        play = False
        
    # Shorten the pause duration slightly
    pause = pause * 0.95
    
    # Pause before the next arrow
    sleep(0.3)
    
# When the loop is exited, display a message with the score

message = "Your score was %s" % score
sense.show_message(message, scroll_speed = 0.05, text_colour = [100, 100, 100])