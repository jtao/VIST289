# Import the processing library for graphics and image manipulation
from processing import *

# Initialize the sketch with settings and assets
def setup():
    # Declare 'img' as a global variable to access it outside this function
    global img
    
    # Set the canvas dimensions to 800 pixels in width and 600 pixels in height
    size(800, 600)
    
    # Load an image named "post_oak.jpg" into the 'img' variable
    img = loadImage("post_oak.jpg")
    
    # Display the loaded image starting from the top-left corner of the canvas
    image(img, 0, 0)

# Continuously execute the code inside to animate or apply real-time effects
def draw():
    # Convert the entire canvas content to grayscale
    filter(GRAY)
