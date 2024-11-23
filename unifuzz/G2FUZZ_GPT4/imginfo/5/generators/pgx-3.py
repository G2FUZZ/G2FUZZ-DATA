import os
import numpy as np
from PIL import Image

def create_high_bit_depth_image(filename, width, height, bit_depth):
    """
    Create an image file with specified width, height, and bit depth.

    :param filename: Name of the file to save (without extension).
    :param width: Width of the image.
    :param height: Height of the image.
    :param bit_depth: Bit depth of the image.
    """
    # Ensure the tmp directory exists
    os.makedirs('./tmp/', exist_ok=True)
    
    # Generate a gradient image data
    img_data = np.zeros((height, width), dtype=np.uint16)
    max_value = (2 ** bit_depth) - 1
    for y in range(height):
        for x in range(width):
            img_data[y, x] = (x + y) % max_value
    
    # Create an image from the data
    img = Image.fromarray(img_data, mode='I;16')
    
    # Saving the image in a format that supports high bit depth (e.g., TIFF)
    tiff_filename = f'./tmp/{filename}.tiff'
    img.save(tiff_filename)

# Example usage
create_high_bit_depth_image('high_bit_depth_image', 256, 256, 16)