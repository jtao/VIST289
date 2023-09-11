# Importing a custom coordinate system module named coordsys
import coordsys as cs

# Setup function for setting initial canvas properties
def setup():
    size(800,800)             # Set canvas size
    background(255)           # Set canvas background color to white
    frameRate(0.2)              # Set frame rate to 1 frame per second

# Draw function runs continuously to render content on the canvas
def draw():
    stroke(0)                 # Set stroke color to black
    background(225)           # Reset canvas background color to near white for every frame

    # Initializing a string to track transformations
    transformation = ""
    
    # Defining the coordinate frame dimensions
    xmin, ymin, xmax, ymax = -10, -10, 10, 10
    
    # Calling custom function to create a coordinate frame
    cs.coordinateFrame(xmin, ymin, xmax, ymax) 

    # Drawing x and y axes lines
    line(xmin, 0, xmax, 0)
    line(0, ymin, 0, ymax)

    # Setting fill color for the rectangle (green with 100 alpha for transparency)
    fill(0, 80, 0, 100) 

    # Drawing the first rectangle
    rect(-2,-1, 4,2)
    
    fill(80, 0, 0, 100) 
    
    # Translation transformation applied every 2nd frame
    if frameCount%2:
        pushMatrix()
        translate(4,4)
        rect(-2,-1, 4,2)
        transformation+="->Translation"
        popMatrix()

    # Rotation transformation applied every 3rd frame
    if frameCount%3:
        pushMatrix()
        rotate(PI/4)
        rect(-2,-1, 4,2)
        transformation+="->Rotation"
        popMatrix()
        

    # Scaling transformation applied every 5th frame
    if frameCount%5:
        pushMatrix()
        scale(2)
        rect(-2,-1, 4,2)
        transformation+="->Scaling"        
        popMatrix()

    # Printing the current frame count and applied transformations
    print(frameCount, transformation)

    # Setting fill color for the second rectangle (red with 100 alpha for transparency)
    # fill(80, 0, 0, 100) 

    # Drawing the second rectangle after transformations
    # rect(-2,-1, 4,2)
