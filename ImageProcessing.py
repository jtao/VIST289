def setup():
    # Initialize the canvas with a width of 800 and a height of 400 pixels
    size(800, 400)
    
    # Declare 'img' and 'processed_img' as global variables to use outside of this function
    global img, processed_img
    
    # Load the viz.png image and assign it to the 'img' variable
    img = loadImage("viz.png")
    
    # Create a new image object 'processed_img' with the same dimensions as 'img', to hold the grayscale version
    processed_img = createImage(img.width, img.height, RGB)
    
    # Get the pixel data of 'img' to be manipulated later
    img.loadPixels()
    
    # Prepare the pixel data of 'processed_img' to be written
    processed_img.loadPixels()
    
    colorMode(RGB, 1)
    # Iterate over each pixel in 'img' and 'processed_img'
    for i in range(len(img.pixels)):
        # Extract the red, green, blue, and alpha values of each pixel in 'img'
        r, g, b, a = red(img.pixels[i]), green(img.pixels[i]), blue(img.pixels[i]), alpha(img.pixels[i])
        
        gray = (r + g +  b) / 3
        
        # Assign the calculated grayscale value to corresponding pixel in 'processed_img'
        processed_img.pixels[i] = color(gray, gray, gray, a)
        
    # Finalize the pixel data modifications in 'processed_img'
    processed_img.updatePixels()

def draw():
    # Fill the canvas with a white background
    background(1)
    
    # Place the original 'img' on the left half of the canvas
    image(img, 0, 0)
    
    # Place the grayscale 'processed_img' on the right half of the canvas
    image(processed_img, img.width, 0)
    
    # Stop any further drawing or animation in the canvas
    noLoop()
