import os
import numpy as np
from PIL import Image

# Ensure the tmp directory exists
os.makedirs('./tmp/', exist_ok=True)

# Create a 100x100 image with direct color support (RGBA)
width, height = 100, 100
data = np.zeros((height, width, 4), dtype=np.uint8)

# Generate a simple pattern: Red and Green gradient with full opacity
for y in range(height):
    for x in range(width):
        # Red gradient from left to right
        data[y, x, 0] = int((x / width) * 255)
        # Green gradient from top to bottom
        data[y, x, 1] = int((y / height) * 255)
        # Full Blue channel
        data[y, x, 2] = 0
        # Full opacity
        data[y, x, 3] = 255

# Create a PIL image from the numpy array
image = Image.fromarray(data, 'RGBA')

# Save the image in a supported format, such as PNG
image.save('./tmp/direct_color_support.png')