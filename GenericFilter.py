from processing import *

def setup():
    global img, result, kernel, current_x, current_y, pixels_per_frame
    size(800, 600)
    img = loadImage("post_oak.jpg")
    image(img, 0, 0)
    
    # ['identity', 'edge_detection', 'box_blur', 'sharpen', 'emboss', 'outline', 
    #   'left_sobel', 'top_sobel', 'laplacian', 'gaussian_blur']
    
    # Define a sample filter (3x3 edge detection kernel)
    kernel = get_kernel_matrix('outline')
    
    result = createImage(img.width, img.height, RGB)
    current_x = 1
    current_y = 1

    frameRate(30)
    pixels_per_frame = 1000 

def draw():
    global current_x, current_y
    for _ in range(pixels_per_frame):
        convolve_one_pixel(current_x, current_y)
        current_x += 1
        if current_x >= img.width - 1:
            current_x = 1
            current_y += 1
        if current_y >= img.height - 1:
            noLoop()  # Stop the animation once all pixels are processed
            break
    image(result, 0, 0)

def get_kernel_matrix(kernel_name):
    kernels = {
        "identity": [
            [0, 0, 0],
            [0, 1, 0],
            [0, 0, 0]
        ],
        "edge_detection": [
            [-1, -1, -1],
            [-1, 8, -1],
            [-1, -1, -1]
        ],
        "box_blur": [
            [1/9., 1/9., 1/9.],
            [1/9., 1/9., 1/9.],
            [1/9., 1/9., 1/9.]
        ],
        "sharpen": [
            [0, -1, 0],
            [-1, 5, -1],
            [0, -1, 0]
        ],
        "emboss": [
            [-2, -1, 0],
            [-1, 1, 1],
            [0, 1, 2]
        ],
        "outline": [
            [1, 1, 1],
            [1, -7, 1],
            [1, 1, 1]
        ],
        "left_sobel": [
            [1, 0, -1],
            [2, 0, -2],
            [1, 0, -1]
        ],
        "top_sobel": [
            [1, 2, 1],
            [0, 0, 0],
            [-1, -2, -1]
        ],
        "laplacian": [
            [0, 1, 0],
            [1, -4, 1],
            [0, 1, 0]
        ],
        "gaussian_blur": [
            [1/16., 2/16., 1/16.],
            [2/16., 4/16., 2/16.],
            [1/16., 2/16., 1/16.]
        ],
        # Add more kernels as needed
    }

    return kernels.get(kernel_name, None)

def convolve_one_pixel(x, y):
    r = g = b = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            col = img.get(x+i, y+j)
            r += red(col) * kernel[j+1][i+1]
            g += green(col) * kernel[j+1][i+1]
            b += blue(col) * kernel[j+1][i+1]
    result.set(x, y, color(r, g, b))
