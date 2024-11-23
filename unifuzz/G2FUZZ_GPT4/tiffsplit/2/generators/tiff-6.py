from PIL import Image
import numpy as np
import os

# Ensure ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Generate an image with an alpha channel (RGBA)
width, height = 256, 256
data = np.zeros((height, width, 4), dtype=np.uint8)

# Create a gradient for the alpha channel from 0 (transparent) to 255 (opaque)
for y in range(height):
    for x in range(width):
        data[y, x] = [x % 256, y % 256, (x+y) % 256, int(255 * (x / width))]  # RGBA

# Create and save the image as TIFF with alpha channel
img = Image.fromarray(data, 'RGBA')
img.save('./tmp/alpha_channel_example.tiff')