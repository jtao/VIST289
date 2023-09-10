# Initialize the picked color to None
picked_color = None

# Set up the initial drawing environment
def setup():
    # Set the canvas size to 800x400 pixels
    size(800, 400)
    # Disable drawing of outlines
    noStroke()
    # Set the color mode to RGB with a maximum value of 255
    colorMode(RGB, 255)
    # Draw the RGB gradient on the left half of the canvas
    draw_rgb_gradient(0, 0, width/2, height)
    frameRate(1)

# Function to draw an RGB gradient
def draw_rgb_gradient(x, y, w, h):
    # Loop through the width of the gradient
    for i in range(w):
        # Map the current loop iteration to an RGB value
        r = map(i, 0, w, 0, 255)
        # Set the fill color for the current rectangle in the gradient
        fill(r, 150, 150)
        # Draw a thin rectangle representing a slice of the gradient
        rect(x + i, y, 1, h)

# Function to draw a circle with color information
def draw_colored_circle(base_color, x, y, diam):
    # Fill the circle with the picked color
    fill(base_color)
    # Draw the circle
    ellipse(x, y, diam, diam)
    
    # Display RGB and HSB values below the circle
    display_rgb_values(base_color, x - diam / 2, y + diam / 2 + 20)
    display_hsb_values(base_color, x - diam / 2, y + diam / 2 + 40)

# Display RGB values at a given position
def display_rgb_values(col, x, y):
    # Extract the red component of the color
    r = red(col)
    # Extract the green component of the color
    g = green(col)
    # Extract the blue component of the color
    b = blue(col)
    # Set the fill color to black
    fill(0)
    # Display the RGB values as text
    text("RGB: (%d, %d, %d)" % (int(r), int(g), int(b)), x, y)

# Display HSB values at a given position
def display_hsb_values(col, x, y):
    # Switch to HSB color mode with a maximum value of 255
    colorMode(HSB, 255)
    # Extract the hue component of the color
    h = hue(col)
    # Extract the saturation component of the color
    s = saturation(col)
    # Extract the brightness component of the color
    b = brightness(col)
    # Set the fill color to black
    fill(0)
    # Display the HSB values as text
    text("HSB: (%d, %d, %d)" % (int(h), int(s), int(b)), x, y)

# Main drawing loop
def draw():
    # Use the global picked_color variable
    global picked_color

    # Check if the mouse is pressed and is on the left half of the canvas
    if mousePressed and mouseX < width/2:
        # Get the color of the pixel where the mouse is pressed
        picked_color = get(mouseX, mouseY)
        
        # Clear the canvas with a white background
        background(255)
        # Redraw the RGB gradient on the left half of the canvas
        draw_rgb_gradient(0, 0, width/2, height)
        
        # Define the diameter for the color information circle
        circle_diameter = min(width, height) / 3
        # Draw the circle with color information on the right half of the canvas
        draw_colored_circle(picked_color, (3 * width) / 4, height / 2, circle_diameter)
