from sense_hat import SenseHat    # Import the Sense Hat module
from random import randint             # This will allow you to choose random numbers for the given variables
from time import sleep                     #

sense = SenseHat()                           # Create the connection to the Sense Hat

# Add a while loop to repeat the code
while True:

    # Create a variable x, and set it equal to a number of your choice between 0 and 7.
    # or use the randint function to choose random coordinate
    # This will be the x coordinate of the pixel on your display.
    # Repeat with another variable called y.
    x = randint(0, 7)
    y = randint(0, 7)

    # Now pick 3 random numbers 0-255, and assign them to r, g, b or use the randint function to choose random colors
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)

    sense.set_pixel(x, y, r, g, b)
    
    sleep(0.01)        # Call sleep function to pause the program
# Do not add the sense.clear() function, this will clear the previous pixel.