import numpy as np
import os
from PIL import Image

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Define image resolution and color depth
width, height = 256, 256
color_depth = 255  # Assuming 8-bit per channel for RGB

# Generate a simple raster image with a gradient
# Create an array of bytes for the image data
image_data = np.zeros((height, width, 3), dtype=np.uint8)

# Fill the image with a gradient
for y in range(height):
    for x in range(width):
        image_data[y, x] = [x % color_depth, y % height, (x+y) % color_depth]

# Use PIL to create an image from the array
image = Image.fromarray(image_data, 'RGB')

# Save the image as a .png file
image.save('./tmp/example.png')