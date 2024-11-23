import numpy as np
import cv2
import os

# Create the ./tmp/ directory if it doesn't exist
if not os.path.exists('./tmp'):
    os.makedirs('./tmp')

# Generating an image with 24-bit color depth
# Creating a 256x256 pixels image with 3 channels (RGB), each channel can hold values from 0-255
# Using numpy to generate an array of unsigned integers (8 bits per channel, thus 24-bit color depth)
width, height = 256, 256
image = np.zeros((height, width, 3), dtype=np.uint8)

# Filling the image with a gradient
# The red channel will vary from left to right, green from top to bottom, and blue will be a mix
for y in range(height):
    for x in range(width):
        image[y, x] = [x, y, (x+y) % 256]  # Modulo 256 to ensure the value is within 0-255

# Save the image using OpenCV
cv2.imwrite('./tmp/gradient_24bit.jpg', image)