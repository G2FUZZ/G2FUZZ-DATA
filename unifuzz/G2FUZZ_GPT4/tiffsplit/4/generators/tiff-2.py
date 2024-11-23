import numpy as np
import os
from PIL import Image

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Create a simple gradient image
width, height = 256, 256
image_data = np.zeros((height, width, 3), dtype=np.uint8)

# Generating a gradient
for x in range(width):
    for y in range(height):
        image_data[y, x] = [x % 256, y % 256, (x+y) % 256]

# Convert numpy array to PIL Image
image = Image.fromarray(image_data, 'RGB')

# Save the image with LZW compression (lossless)
image.save('./tmp/gradient_lossless_compression.tiff', compression='tiff_lzw')