import os
import numpy as np
from PIL import Image

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Generate a horizontal gradient image
width, height = 256, 256
image_data = np.zeros((height, width, 3), dtype=np.uint8)

# Create gradient
for x in range(width):
    for y in range(height):
        image_data[y, x] = [x, x, x]  # RGB channels

# Save the image
img = Image.fromarray(image_data, 'RGB')
img.save(f'./tmp/gradient.png', format='PNG', compress_level=9)

print("Image saved.")