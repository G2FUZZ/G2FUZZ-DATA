import numpy as np
from PIL import Image
import os

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Generate a simple gradient image
width, height = 800, 600
image = np.zeros((height, width, 3), dtype=np.uint8)

# Create a vertical gradient
for y in range(height):
    r, g, b = y // 2, y // 3, y // 4
    image[y, :, 0] = r
    image[y, :, 1] = g
    image[y, :, 2] = b

# Convert the numpy array to a PIL image
img = Image.fromarray(image, 'RGB')

# Save the image as JPEG, which will use lossy compression
img.save('./tmp/gradient_image.jpg', 'JPEG')