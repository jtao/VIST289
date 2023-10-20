# Importing necessary modules and classes
import coordsys as cs
from math import cos, sin, radians

# Define a 2D vector or point class
class Vect2D:
    # Constructor to initialize x and y values
    def __init__(self, x=0, y=0):  
        self.x = x
        self.y = y

    # Define a formatted output for print()
    def __str__(self):  
        return '(%s, %s)' % (self.x, self.y)

# Define a 2D Homogeneous matrix class
class Matrix2DH:
    # Constructor to initialize the matrix
    def __init__(self, diag=1.0):  
        self.rows = [[diag, 0, 0],
                     [0, diag, 0],
                     [0, 0, diag]]

    # Define a formatted output for print()
    def __str__(self):  
        return '\n'.join([' '.join(["%7.3f" % (item) for item in row]) for row in self.rows])

    # Define matrix multiplication method
    def matmult(self, mat):  
        newmat = Matrix2DH(0.0)  # Initialize a new matrix
        for row in range(3):
            for col in range(3):
                for rc in range(3):
                    newmat.rows[row][col] += self.rows[row][rc] * mat.rows[rc][col]
        return newmat

    # Define vector multiplication method
    def vecmult(self, vect):  
        newvect = Vect2D()  # Initialize a new vector
        newvect.x = self.rows[0][0] * vect.x + self.rows[0][1] * vect.y + self.rows[0][2]
        newvect.y = self.rows[1][0] * vect.x + self.rows[1][1] * vect.y + self.rows[1][2]
        return newvect

    # Define rotation method
    def rotate(self, theta):  
        c = cos(radians(theta))  # Calculate cosine of the angle
        s = sin(radians(theta))  # Calculate sine of the angle
        rot = Matrix2DH()  # Initialize a new matrix
        rot.rows = [[c, -s, 0.0], [s, c, 0.0], [0.0, 0.0, 1.0]]  # Define rotation matrix
        return self.matmult(rot)  # Return the result of matrix multiplication

    # Define translation method
    def translate(self, dx):  
        xlate = Matrix2DH()  # Initialize a new matrix
        xlate.rows[0][2] = dx.x  # Set the translation for x
        xlate.rows[1][2] = dx.y  # Set the translation for y
        return self.matmult(xlate)  # Return the result of matrix multiplication

def draw_coord():  
    # Define a method to draw the coordinate system

    stroke(0)  # Set stroke color to black
    background(225)  # Reset canvas background color to near white for every frame

    # Define the coordinate frame dimensions
    xmin, ymin, xmax, ymax = -10, -10, 10, 10

    # Call custom function to create a coordinate frame
    cs.coordinateFrame(xmin, ymin, xmax, ymax)

    # Draw x and y axes lines
    line(xmin, 0, xmax, 0)
    line(0, ymin, 0, ymax)

    # Set fill color for the rectangle (green with 100 alpha for transparency)
    fill(0, 80, 0, 100)

# Initialize triangle vertices as a list of Vect2D objects
triangle_vertices = [Vect2D(-2.5, -5 * sqrt(3) / 6), Vect2D(2.5, -5 * sqrt(3) / 6), Vect2D(0, 5 * sqrt(3) / 3)]

def setup():  
    # Define the setup method for the sketch

    size(800, 800)  # Set canvas size
    background(255)  # Set canvas background color to white

    draw_coord()  # Call method to draw the coordinate system

    global triangle_vertices  # Access the global variable

    # Draw original triangle in blue
    fill(0, 0, 255)
    beginShape()  # Begin drawing a shape
    for vert in triangle_vertices:
        vertex(vert.x, vert.y)  # Draw vertices of the triangle
    endShape(CLOSE)  # End drawing the shape and close it

def draw():  
    # Define the draw method for the sketch

    global triangle_vertices  # Access the global variable
    draw_coord()  # Call method to draw the coordinate system
    I = Matrix2DH()  # Initialize a new matrix

    if frameCount < 360:  
        # If the frame count is less than 360
        theta = frameCount  # Set theta as the frame count
        r = I.rotate(theta)  # Rotate the matrix by theta degrees
        transformed_vertices = [r.vecmult(vert) for vert in triangle_vertices]  # Multiply the rotated matrix with each vertex

        # Draw rotated triangle in blue
        fill(0, 0, 255)
        beginShape()  # Begin drawing a shape
        for vert in transformed_vertices:
            vertex(vert.x, vert.y)  # Draw vertices of the rotated triangle
        endShape(CLOSE)  # End drawing the shape and close it

    elif frameCount < 720:  
        # If the frame count is between 360 and 720
        theta = 360  # Set theta as 360
        trans_amount = (frameCount - theta) / 100.0  # This will start from 1 and increase
        trans_vector = Vect2D(trans_amount, trans_amount)  # Create a new vector for translation
        RT = I.translate(trans_vector)  # Translate the matrix by the vector
        transformed_vertices = [RT.vecmult(vert) for vert in triangle_vertices]  # Multiply the translated matrix with each vertex

        # Draw translated triangle in red
        fill(255, 0, 0)
        beginShape()  # Begin drawing a shape
        for vert in transformed_vertices:
            vertex(vert.x, vert.y)  # Draw vertices of the translated triangle
        endShape(CLOSE)  # End drawing the shape and close it

    else:  
        # If the frame count is 720 or more
        noLoop()  # Stop the draw loop
