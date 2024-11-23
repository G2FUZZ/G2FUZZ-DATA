import os
from PIL import Image
import numpy as np

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Function to create a BMP file with the specified color depth
def create_bmp_file(color_depth, width=100, height=100):
    # Depending on the color depth, generate an appropriate image
    if color_depth == 1:  # 1-bit monochrome
        mode = '1'  # 1-bit pixels, black and white, stored with one pixel per byte
    elif color_depth == 4:  # 4-bit color
        mode = 'P'  # 8-bit pixels, mapped to any other mode using a color palette
        width, height = 100, 100  # Ensuring the image size is compatible
    elif color_depth == 8:  # 8-bit color
        mode = 'P'  # Using palette mode for 256 colors
    elif color_depth == 16:  # 16-bit color
        # PIL doesn't support 16-bit directly in a way that's easy to demonstrate color depth, using RGB instead
        mode = 'RGB'
        width, height = 100, 100
    elif color_depth == 24:  # 24-bit color
        mode = 'RGB'
    elif color_depth == 32:  # 32-bit color
        mode = 'RGBA'
    else:
        return "Unsupported color depth"

    # Generating a gradient for demonstration purposes
    if mode in ['RGB', 'RGBA']:
        # For RGB(A), create an array and fill it with a gradient
        image_data = np.zeros((height, width, len(mode)), dtype=np.uint8)

        for y in range(image_data.shape[0]):
            for x in range(image_data.shape[1]):
                image_data[y, x] = [x % 256, y % 256, (x + y) % 256, 255] if mode == 'RGBA' else [x % 256, y % 256, (x + y) % 256]
    else:
        # For '1' or 'P', create an image with a simple pattern or gradient
        image = Image.new(mode, (width, height))
        image_data = np.array(image)

        # Fill the image data with a pattern
        for y in range(height):
            for x in range(width):
                image_data[y, x] = (x + y) % 256 if mode == 'P' else (x % 2 and y % 2)

        image = Image.fromarray(image_data, mode)

    if mode not in ['1', 'P']:
        image = Image.fromarray(image_data, mode)

    # Save the image to a file
    filename = f'./tmp/bmp_{color_depth}bit.bmp'
    image.save(filename, 'BMP')

# Example color depths to generate
color_depths = [1, 4, 8, 16, 24, 32]

for depth in color_depths:
    create_bmp_file(depth)