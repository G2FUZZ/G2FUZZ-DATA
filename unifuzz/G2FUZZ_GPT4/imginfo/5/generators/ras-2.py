import numpy as np
import os
from PIL import Image

# Directory for saving the files
output_dir = './tmp/'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Function to create an image and save as PNG format
def create_png_image(filename, color_depth):
    # Create an array of random colors
    if color_depth == 1:
        # For 1-bit images, only black and white
        data = np.random.randint(0, 2, (100, 100), dtype=np.bool)
        mode = '1'
    elif color_depth == 8:
        # For 8-bit images, 256 colors (grayscale)
        data = np.random.randint(0, 256, (100, 100), dtype=np.uint8)
        mode = 'L'
    elif color_depth == 24:
        # For 24-bit images, true color
        data = np.random.randint(0, 256, (100, 100, 3), dtype=np.uint8)
        mode = 'RGB'
    else:  # Assuming 32 bit (RGBA)
        data = np.random.randint(0, 256, (100, 100, 4), dtype=np.uint8)
        mode = 'RGBA'
    
    # Create an image from the data
    img = Image.fromarray(data, mode=mode)
    # Save the image in PNG format
    img.save(os.path.join(output_dir, f'{filename}.png'))

# Create images with various color depths
create_png_image('1bit_image', 1)
create_png_image('8bit_image', 8)
create_png_image('24bit_image', 24)
create_png_image('32bit_image', 32)