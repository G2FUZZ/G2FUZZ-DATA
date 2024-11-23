import numpy as np
from PIL import Image, TiffImagePlugin
import os

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Function to create a gradient image array
def create_gradient_image(width, height):
    array = np.zeros((height, width, 3), dtype=np.uint8)
    for i in range(height):
        for j in range(width):
            array[i, j] = [i % 256, j % 256, (i+j) % 256]
    return array

# Multi-page TIFF creation with various compression schemes
def create_complex_tiff(filename):
    width, height = 256, 256

    # List of compression schemes for demonstration
    compression_schemes = ['tiff_lzw', 'jpeg', 'tiff_adobe_deflate']

    with TiffImagePlugin.AppendingTiffWriter(filename, True) as tf:
        for compression in compression_schemes:
            # Create a sample gradient image for each compression scheme
            img_array = create_gradient_image(width, height)
            img = Image.fromarray(img_array)

            # Save the current page/image with specific compression
            img.save(tf, format='TIFF', compression=compression)

            # Attempting to add custom tags or metadata should be done here,
            # but Pillow's API may not support complex TIFF tag manipulations directly.

# Create a complex TIFF file
create_complex_tiff('./tmp/complex_sample.tiff')