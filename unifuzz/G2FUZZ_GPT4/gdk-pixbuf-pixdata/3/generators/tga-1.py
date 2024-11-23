import os
import numpy as np

def create_tga_image(data, filename, color_depth):
    """
    Create a TGA image file from data.

    Args:
    - data: numpy array of image data.
    - filename: Name of the file to save.
    - color_depth: The color depth of the image (8, 24, or 32 bit).
    """
    header = bytearray(18)
    header[2] = 2  # Image type code - uncompressed true-color image
    header[12] = data.shape[1] & 0xFF
    header[13] = (data.shape[1] >> 8) & 0xFF
    header[14] = data.shape[0] & 0xFF
    header[15] = (data.shape[0] >> 8) & 0xFF
    header[16] = color_depth  # Color depth

    with open(filename, 'wb') as f:
        f.write(header)
        data.tofile(f)

# Ensure the tmp directory exists
os.makedirs('./tmp/', exist_ok=True)

# Generate a simple 8-bit (grayscale) image
width, height = 100, 100
gray_image = np.random.randint(0, 256, (height, width), dtype=np.uint8)
create_tga_image(gray_image, './tmp/gray_image.tga', 8)  # Corrected variable name here

# Generate a simple 24-bit (RGB) image
rgb_image = np.random.randint(0, 256, (height, width, 3), dtype=np.uint8)
create_tga_image(rgb_image, './tmp/rgb_image.tga', 24)

# Generate a 32-bit (RGBA) image with an alpha channel
rgba_image = np.random.randint(0, 256, (height, width, 4), dtype=np.uint8)
create_tga_image(rgba_image, './tmp/rgba_image.tga', 32)