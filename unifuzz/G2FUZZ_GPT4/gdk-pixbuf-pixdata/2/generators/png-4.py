import os
import numpy as np
from PIL import Image

# Ensure the target directory exists
os.makedirs('./tmp/', exist_ok=True)

# Generate a simple gradient image
width, height = 256, 256
image_data = np.zeros((height, width, 3), dtype=np.uint8)
for y in range(height):
    for x in range(width):
        image_data[y, x] = [x, y, (x+y)//2]

# Create an Image object
image = Image.fromarray(image_data, 'RGB')

# Save the image with Adam7 interlacing
image.save('./tmp/interlaced_image.png', 'PNG', interlace=True)