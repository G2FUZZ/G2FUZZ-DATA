from PIL import Image
import numpy as np
import os

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Generate a 256x256 pixels image with a gradient
width, height = 256, 256
image = np.zeros((height, width), dtype=np.uint8)

# Creating a gradient effect for our image
for i in range(height):
    for j in range(width):
        image[i, j] = (i+j) % 256

# Convert the numpy array to a PIL image
img = Image.fromarray(image)

# Save the image with LZW compression
# Note: The 'compression' argument is used to specify the compression method.
# The 'tiffinfo' argument was removed since it's not supported.
img.save('./tmp/gradient_lzw_compressed_with_halftoning.tiff', compression='tiff_lzw')