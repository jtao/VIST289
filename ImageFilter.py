# Import the required library
from processing import *

# Setup function to define canvas and load image
def setup():
    global img
    size(800, 600)
    img = loadImage("post_oak.jpg")  # Replace with your image path
    image(img, 0, 0)
    
# Draw function to apply filters
# You can uncomment each line below to try things out.

def draw():

        # Grayscale Conversion
#    filter(GRAY)
#    filter(INVERT)

# The range for the levels parameter is typically between 2 and 255:
#    filter(POSTERIZE, 2)

# Commonly used values might range from 0 to 67.
#    filter(BLUR, 67)
    
# Sets the alpha channel to entirely opaque.
#    filter(OPAQUE)

# Reduces the light areas.
#    filter(ERODE)
    
# Increases the light areas
#    filter(DILATE)

# The threshold level parameter ranges from 0.0 to 1.0.
    filter(THRESHOLD, 0.3)

    noLoop()
