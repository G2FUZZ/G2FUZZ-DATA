import numpy as np
from PIL import Image
import os

# Ensure the ./tmp/ directory exists
output_dir = "./tmp/"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Define pixel data
# Let's create a simple image with RGBA (Red, Green, Blue, Alpha) format
# For demonstration, creating a 10x10 image with a gradient and alpha value

width, height = 10, 10
data = np.zeros((height, width, 4), dtype=np.uint8)

# Creating a gradient for red channel and full green with varying alpha
for y in range(height):
    for x in range(width):
        data[y, x] = [x * 25, 255, 0, y * 25]  # RGBA

# Create an image from the data
img = Image.fromarray(data, 'RGBA')

# Save the image
filename = os.path.join(output_dir, "pixdata.png")
img.save(filename)

print(f"Saved pixel data to {filename}")