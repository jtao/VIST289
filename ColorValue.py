# Declare a global variable to hold the image data.
img = None

# Define a scaling factor to resize elements for better visibility.
sf = 40

# Set up the drawing environment.
def setup():
    # Access the global 'img' variable.
    global img
    
    # Set the size of the canvas based on the scaling factor.
    size(15 * sf, 12 * sf)
    
    # Load the image file into the 'img' variable.
    img = loadImage("viz_logo.png")
    
    # Resize the image to the desired dimensions.
    img.resize(15, 12)
    
    # Make sure the draw function is called only once.
    noLoop()

# Define the main drawing function.
def draw():
    # Set the background color to white.
    background(255)
    
    # Iterate over each pixel in the image's width.
    for x in range(img.width):
        # Iterate over each pixel in the image's height.
        for y in range(img.height):
            # Get the color of the current pixel.
            pixel_color = img.get(x, y)
            
            # Determine the brightness (or grayscale value) of the pixel color.
            brightness_value = int(brightness(pixel_color))
            
            # Set the fill color for the rectangle to the pixel color.
            fill(pixel_color)
            
            # Ensure there's no outline for the rectangle.
            noStroke()
            
            # Draw a rectangle representing the current pixel, scaled up for better visibility.
            rect(x*sf, y*sf, sf, sf)
            
            # Set the fill color for the text based on pixel brightness (to ensure the text is visible).
            fill(255 if brightness_value < 128 else 0)
            
            # Set the text size and alignment.
            textSize(10)
            textAlign(CENTER, CENTER)
            
            # Display the inverted brightness value on the pixel.
            text(str(255 - brightness_value), x*sf + 10, y*sf + 10)
