import os
import numpy as np
from PIL import Image

# Create the tmp directory if it doesn't exist
os.makedirs('./tmp/', exist_ok=True)

# Generate an image with Adam7 interlacing
width, height = 256, 256
channels = 3  # RGB
data = np.zeros((height, width, channels), dtype=np.uint8)

# Create a gradient effect for demonstration
for y in range(height):
    for x in range(width):
        data[y, x] = [x % 256, y % 256, (x + y) % 256]

# Create an image from the array
image = Image.fromarray(data)

# Save the image with Adam7 interlacing
image.save('./tmp/interlaced_adam7.png', 'PNG', interlace=True)