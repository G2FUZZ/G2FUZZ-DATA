import os
from PIL import Image
import numpy as np

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Define image dimensions
width, height = 100, 100

# Generate a simple gradient from bottom to top
# Since the BMP format stores pixels from bottom to top, we generate accordingly
gradient = np.zeros((height, width, 3), dtype=np.uint8)
for i in range(height):
    gradient[i, :, :] = i * 255 // height

# Convert the Numpy array to an image
image = Image.fromarray(gradient, 'RGB')

# Save the image as BMP
image.save('./tmp/gradient.bmp')