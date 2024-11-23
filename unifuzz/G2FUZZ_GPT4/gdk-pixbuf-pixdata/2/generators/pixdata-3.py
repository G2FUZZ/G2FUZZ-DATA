import numpy as np
from PIL import Image

# Create an image with RGBA mode (supporting transparency)
width, height = 200, 200
# Creating an array of random colors and adding a random alpha channel for transparency
data = np.random.rand(height, width, 4) * 255
# Ensure that the data type is uint8
data = data.astype(np.uint8)

# Create an image from the array
img = Image.fromarray(data, 'RGBA')

# Ensure the ./tmp/ directory exists
import os
if not os.path.exists('./tmp/'):
    os.makedirs('./tmp/')

# Save the image
img.save('./tmp/transparency_support_pixdata.png')