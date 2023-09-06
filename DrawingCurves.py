# Import all functions and classes from the coordsys module
import coordsys as cs

# setup() function runs once at the beginning to initialize variables and settings
def setup():
    global t, ptlist
    # Initialize canvas size to 800x600 pixels
    size(600, 600)
    
    # Set color mode to RGB with values ranging from 0.0 to 1.0
    # e.g., TAMU Maroon (80, 0 ,0) will be (0.3137254901960784, 0, 0)
    
    colorMode(RGB, 1.0, 1.0, 1.0)
    
    # Set stroke color to a light yellow
    # Let's change the color to TAMU Maroon
    stroke(1.0, 1.0, 0.4)

    # Set fill color to a light blue
    fill(0.4, 0.4, 1.0)
    
    # Initialize parameter t with 0.0
    t = 0.0
    # Initialize ptlist (a list to store points) as an empty list
    ptlist = []
    frameRate(30)
    
# draw() function runs repeatedly to update the canvas
def draw():
    global t, ptlist
    # Set up a custom coordinate frame (a function defined in coordsys)
    # coordinateFrame(xmin, ymin, xmax, ymax) sets up the drawing coordinate system so 
    # that xmin is on the lefthand side of the window xmax on the righthand, ymin on the 
    # bottom, and ymax on the top. It also redefines the stroke weight to be one pixel, 
    # otherwise it would scale up or down due to the scale operation. The global view 
    # plane width is used to communicate the width, in drawing coordinates, of the window.    
    cs.coordinateFrame(-16, -16, 16, 16)
    
    # Set the border weight for shapes
    cs.borderWeight(3)
    
    # Set the background color to a purplish shade
    background(0.25, 0.0, 0.1)
    
    # Add a new point to ptlist with x-coordinate t and y-coordinate 3.0
    ptlist.append((16*(sin(t)**3), 13*cos(t) - 5*cos(2*t)- 2*cos(3*t) - cos(4*t)))
    
    # Initialize lastpt with the first point in ptlist
    lastpt = ptlist[0]
    # Iterate through the remaining points in ptlist
    for newpt in ptlist[1:]:
        # Draw a line from lastpt to newpt
        line(lastpt[0], lastpt[1], newpt[0], newpt[1])
        # Update lastpt to the current newpt
        lastpt = newpt
    
    # Increment t by 0.025 in each iteration
    t += 0.025
    
    # Check if t has exceeded 8.0
    if t > 8.0:
        # Stop the draw loop to prevent further updates
        noLoop()
