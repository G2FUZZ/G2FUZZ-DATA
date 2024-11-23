import numpy as np
from PIL import Image
import os

# Ensure tmp directory exists
output_dir = './tmp/'
os.makedirs(output_dir, exist_ok=True)

# Generate an image with an alpha channel (RGBA)
width, height = 256, 256
data = np.zeros((height, width, 4), dtype=np.uint8)

# Fill the image with a gradient and an example pattern
# Red gradient on X, green gradient on Y, solid blue, and a transparency gradient
for y in range(height):
    for x in range(width):
        data[y, x] = [x, y, 128, x % 128 + y % 128]  # RGBA

# Create and save the image
img = Image.fromarray(data, 'RGBA')
img.save(os.path.join(output_dir, 'pixdata_with_alpha.png'))