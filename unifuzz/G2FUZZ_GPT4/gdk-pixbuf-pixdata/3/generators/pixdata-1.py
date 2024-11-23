import os
import numpy as np
from PIL import Image

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Create a 100x100 image with a gradient from black to red
width, height = 100, 100
image = np.zeros((height, width, 3), dtype=np.uint8)

# Generating gradient
for x in range(width):
    for y in range(height):
        image[y, x, 0] = (x + y) // 2  # Red channel

# Create an image object
img = Image.fromarray(image)

# Save the pixel data to a file in raw format
pixdata_path = './tmp/image_pixdata.pix'
with open(pixdata_path, 'wb') as f:
    pixel_data = img.tobytes()
    f.write(pixel_data)

print(f"File saved to {pixdata_path}")