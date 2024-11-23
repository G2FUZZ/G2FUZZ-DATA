import numpy as np
import os
from PIL import Image

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Generate a bitmap image data
width, height = 256, 256  # Define the dimensions of the image
data = np.zeros((height, width, 3), dtype=np.uint8)

# Create a simple pattern on the image
for y in range(height):
    for x in range(width):
        data[y, x] = [x % 256, y % 256, (x*y) % 256]

# Convert the numpy array to an image
image = Image.fromarray(data)

# Save the image as a PNG file instead of RAS
image.save('./tmp/generated_image.png')