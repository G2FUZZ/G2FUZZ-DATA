import os
from PIL import Image
import numpy as np

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Function to generate an image with given color depth
def generate_image(color_depth, filename):
    width, height = 256, 256  # Image dimensions

    if color_depth == 1:
        # Generate a monochrome image (1-bit)
        mode = '1'
        image = Image.new(mode, (width, height), 0)
        # Draw a simple pattern
        for x in range(width):
            for y in range(height):
                if (x // 32 + y // 32) % 2 == 0:
                    image.putpixel((x, y), 1)
    elif color_depth in [4, 8]:
        # Generate a 4-bit or 8-bit grayscale image
        mode = 'P'
        image = Image.new(mode, (width, height))
        # Create a gradient
        for x in range(width):
            for y in range(height):
                value = x * 255 // width if color_depth == 8 else x * 15 // width
                image.putpixel((x, y), value)
    elif color_depth == 16:
        # Generate a 16-bit image (5 bits red, 6 bits green, 5 bits blue)
        mode = 'RGB'
        image_array = np.zeros((height, width, 3), dtype=np.uint8)
        # Create a gradient
        for x in range(width):
            for y in range(height):
                image_array[y, x] = [(x * 31) // width, (x * 63) // width, (y * 31) // height]
        image = Image.fromarray(image_array)
    elif color_depth == 24:
        # Generate a 24-bit RGB image
        mode = 'RGB'
        image_array = np.zeros((height, width, 3), dtype=np.uint8)
        # Create a colorful pattern
        for x in range(width):
            for y in range(height):
                image_array[y, x] = [(x * 255) // width, (y * 255) // height, 128]
        image = Image.fromarray(image_array)
    elif color_depth == 32:
        # Generate a 32-bit RGBA image
        mode = 'RGBA'
        image_array = np.zeros((height, width, 4), dtype=np.uint8)
        # Create a semi-transparent gradient
        for x in range(width):
            for y in range(height):
                image_array[y, x] = [(x * 255) // width, (y * 255) // height, 128, (x * 255) // width]
        image = Image.fromarray(image_array)

    # Save the image
    image.save(filename)

# Generate and save images for each color depth
color_depths = [1, 4, 8, 16, 24, 32]
for depth in color_depths:
    generate_image(depth, f'./tmp/{depth}-bit.bmp')