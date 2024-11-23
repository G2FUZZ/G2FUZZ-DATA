from PIL import Image
import numpy as np
import os

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Image size
width, height = 300, 300

# Creating an RGBA image (Red, Green, Blue, Alpha)
image = np.zeros((height, width, 4), dtype=np.uint8)

# Fill the image: simple gradient for demonstration
for x in range(width):
    for y in range(height):
        # Setting Red to maximum, Green and Blue to gradients, and a gradient Alpha
        image[y, x] = [255, x % 256, y % 256, int(255 * (x / width))]

# Convert the numpy array to PIL Image
img = Image.fromarray(image, 'RGBA')

# Save the image as TIFF with an alpha channel
img.save('./tmp/alpha_channel_image.tiff')

print("TIFF image with alpha channel saved successfully.")