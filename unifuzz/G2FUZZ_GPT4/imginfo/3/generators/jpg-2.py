import numpy as np
import cv2
import os

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Generate an image with 24-bit color depth
# Creating a 256x256 image with 3 channels (RGB), each channel can have values from 0-255
# This will create a gradient image showcasing a wide range of colors
width, height = 256, 256
image = np.zeros((height, width, 3), dtype=np.uint8)

# Fill the image with a gradient
for y in range(height):
    for x in range(width):
        image[y, x] = [x % 256, y % 256, (x*y) % 256]

# Save the image as a JPG file with 24-bit color depth in the ./tmp/ directory
cv2.imwrite('./tmp/gradient_image.jpg', image)