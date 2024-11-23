from PIL import Image
import numpy as np
import os

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Create an image using numpy (for demonstration purposes, we'll create a gradient image)
width, height = 256, 256
image_data = np.zeros((height, width, 3), dtype=np.uint8)
for x in range(width):
    for y in range(height):
        image_data[y, x] = [x, y, (x+y) // 2]

# Convert the numpy array to a PIL image
image = Image.fromarray(image_data, 'RGB')

# Save the image with LZW compression which is lossless
image.save('./tmp/lossless_compressed_image.tiff', compression='tiff_lzw')