import os
from PIL import Image
import numpy as np

# Ensure the ./tmp/ directory exists
output_dir = './tmp/'
os.makedirs(output_dir, exist_ok=True)

# Feature 8: Wide Tool Support
# Generate an image to represent "Wide Tool Support"
# For simplicity, we'll create an image with a basic pattern

# Image dimensions and pattern
width, height = 300, 200
channels = 3  # RGB
color1 = [255, 215, 0]  # Gold
color2 = [0, 191, 255]  # Deep Sky Blue

# Create an array to hold the pixel data
image_data = np.zeros((height, width, channels), dtype=np.uint8)

# Fill the image with a simple pattern
for y in range(height):
    for x in range(width):
        if (x // 50) % 2 == (y // 50) % 2:
            image_data[y, x] = color1
        else:
            image_data[y, x] = color2

# Convert the array to an image
image = Image.fromarray(image_data)

# Save the image as a PNM file (PPM format in this case)
image_path = os.path.join(output_dir, 'wide_tool_support.ppm')
image.save(image_path)

print(f"Generated PNM file saved to: {image_path}")