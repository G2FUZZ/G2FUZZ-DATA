import os
import numpy as np
from PIL import Image, ImageDraw

# Ensure the tmp directory exists
if not os.path.exists('./tmp'):
    os.makedirs('./tmp')

# Create an image with a simple binary format: white and black pixels
width, height = 200, 200  # Size of the image
image = Image.new('1', (width, height), "white")  # '1' for 1-bit pixels, black and white
draw = ImageDraw.Draw(image)

# Draw a simple pattern: a checkerboard for example
def draw_checkerboard(draw, width, height, cell_size):
    for y in range(0, height, cell_size):
        for x in range(0, width, cell_size):
            if (x + y) // cell_size % 2 == 0:
                draw.rectangle([x, y, x + cell_size - 1, y + cell_size - 1], fill="black")

cell_size = 20
draw_checkerboard(draw, width, height, cell_size)

# Save the image as a GIF
image.save('./tmp/simple_binary_format.gif')