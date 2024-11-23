import os
import numpy as np
from PIL import Image

# Create the tmp directory if it doesn't exist
os.makedirs('./tmp/', exist_ok=True)

# Generate an image
width, height = 256, 256
data = np.zeros((height, width, 3), dtype=np.uint8)

# Create a simple gradient
for y in range(height):
    for x in range(width):
        data[y, x] = [x % 256, y % 256, (x*y) % 256]

# Create an image from the array
image = Image.fromarray(data, 'RGB')

# Apply Adam7 interlacing
image.save('./tmp/interlaced_image.png', 'PNG', interlace=True)