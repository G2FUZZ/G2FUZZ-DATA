import os
import numpy as np
from PIL import Image

# Creating a directory if it doesn't exist
directory = './tmp/'
if not os.path.exists(directory):
    os.makedirs(directory)

def generate_radial_gradient(width, height, bits):
    """
    Generates a radial gradient from the center of the image.
    """
    center_x, center_y = width // 2, height // 2
    max_radius = np.sqrt(center_x**2 + center_y**2)
    if bits == 32:
        # Initialize array with an extra dimension for alpha channel
        array = np.zeros((height, width, 4), dtype=np.uint8)
    else:
        array = np.zeros((height, width, 3), dtype=np.uint8)
    for y in range(height):
        for x in range(width):
            # Distance to the center
            distance = np.sqrt((x - center_x)**2 + (y - center_y)**2)
            # Normalized distance as a color value
            value = 255 - int(255 * (distance / max_radius))
            if bits == 32:
                # For 32-bit, include the alpha channel
                array[y, x] = [value, value // 2, value, 255]
            else:
                array[y, x] = [value, value // 2, value]
    return array

def generate_checkerboard(width, height, cell_size):
    """
    Generates a checkerboard pattern.
    """
    array = np.zeros((height, width, 3), dtype=np.uint8)
    for y in range(height):
        for x in range(width):
            if (x // cell_size) % 2 == (y // cell_size) % 2:
                array[y, x] = [255, 255, 255]
            else:
                array[y, x] = [0, 0, 0]
    return array

def generate_complex_bmp_files():
    width, height = 256, 256
    cell_size = 32  # For checkerboard pattern

    for bits in [1, 4, 8, 16, 24, 32]:
        if bits in [1, 4, 8]:
            # Generating a simple gradient for lower color depths
            array = np.zeros((height, width), dtype=np.uint8)
            for i in range(height):
                for j in range(width):
                    array[i, j] = 255 * (i + j) // (width + height - 2)
            image = Image.fromarray(array, 'L')
        elif bits == 16:
            # Generate a checkerboard pattern for 16-bit
            array = generate_checkerboard(width, height, cell_size)
            image = Image.fromarray(array, 'RGB')
        elif bits == 24:
            # Generate a radial gradient for 24-bit
            array = generate_radial_gradient(width, height, bits)
            image = Image.fromarray(array, 'RGB')
        elif bits == 32:
            # Generate a radial gradient with transparency for 32-bit
            array = generate_radial_gradient(width, height, bits)
            image = Image.fromarray(array, 'RGBA')

        # Save the image as BMP with a descriptive filename
        filename = f'{directory}complex_color_depth_{bits}_bit.bmp'
        image.save(filename, 'BMP')

# Generate and save the BMP files with complex patterns
generate_complex_bmp_files()