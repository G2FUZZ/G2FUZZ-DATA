from PIL import Image
import numpy as np
import os

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Create an image with 24-bit color depth (8 bits per channel, RGB)
width, height = 800, 600
image = np.zeros((height, width, 3), dtype=np.uint8)

# Generating a gradient
for x in range(width):
    for y in range(height):
        image[y, x] = [x % 256, y % 256, (x + y) % 256]

# Convert the array to an Image
img = Image.fromarray(image, 'RGB')

# Save the image
img.save('./tmp/gradient_image.jpg')