import os
from PIL import Image
import numpy as np

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Create an image
width, height = 256, 256
data = np.zeros((height, width, 3), dtype=np.uint8)

# Generate a gradient
for x in range(width):
    for y in range(height):
        data[y, x] = [x % 256, y % 256, (x * y) % 256]

# Create an Image object
img = Image.fromarray(data, 'RGB')

# Save the image with RLE compression for demonstration
# Note: PIL/Pillow does not support RLE compression for BMP directly.
# We save without compression as BMP does not support RLE for 24-bit images natively through Pillow.
img.save('./tmp/gradient_no_compression.bmp')

# If you need to work with 8-bit images and experiment with RLE compression,
# you would typically need to work at a lower level than Pillow provides,
# or convert the image to a format that supports RLE and manually manipulate the file.
# This is an advanced task and goes beyond basic PIL/Pillow usage.