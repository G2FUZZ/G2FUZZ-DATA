import os
from PIL import Image
import numpy as np

# Creating a directory if it doesn't exist
directory = './tmp/'
if not os.path.exists(directory):
    os.makedirs(directory)

# Function to generate BMP files with different color depths
def generate_bmp_files():
    # Define image size
    width, height = 256, 256

    # Generate an image for each color depth
    for bits in [1, 4, 8, 16, 24, 32]:
        # Creating a gradient for demonstration purposes
        if bits in [1, 4, 8]:
            # For lower color depths, use a simple gradient
            array = np.zeros((height, width), dtype=np.uint8)
            for i in range(height):
                for j in range(width):
                    array[i, j] = 255 * (i + j) // (width + height - 2)
            if bits == 1 or bits == 4:
                # For 1-bit and 4-bit color depth, PIL expects an 8-bit array but will use a mode that reflects the desired bit depth
                # No additional changes needed here as PIL can handle 8-bit arrays for grayscale images
                pass
            elif bits == 8:
                # For 8-bit, we already have the gradient suited for 256 colors
                pass
        else:
            # For higher color depths, generate a more complex gradient
            array = np.zeros((height, width, 3), dtype=np.uint8)
            for i in range(height):
                for j in range(width):
                    if bits == 16:
                        # Simulate 16-bit color depth by reducing the color palette
                        r, g, b = (i * 255 // height) >> 3, (j * 255 // width) >> 2, (i * 255 // height) >> 3
                        array[i, j] = [r << 3, g << 2, b << 3]
                    elif bits == 24 or bits == 32:
                        # Full color for 24-bit and 32-bit
                        array[i, j] = [i * 255 // height, j * 255 // width, 128]

        # Convert array to an image
        if bits in [1, 4, 8]:
            image = Image.fromarray(array, 'L')  # 'L' mode for grayscale images
        else:
            image = Image.fromarray(array, 'RGB')  # 'RGB' mode for color images

        if bits == 32:
            # Add an alpha channel for 32-bit images
            alpha = Image.new('L', (width, height), color=255)  # Fully opaque
            image.putalpha(alpha)

        # Save the image as BMP with a descriptive filename
        filename = f'{directory}color_depth_{bits}_bit.bmp'
        image.save(filename, 'BMP')

# Generate and save the BMP files
generate_bmp_files()