import os
from PIL import Image
import numpy as np

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Define the image size and color (RGB)
width, height = 640, 480
color = (255, 0, 0)  # Red, change as needed

# Create a numpy array with the defined color
# The array represents the image with the shape (height, width, 3).
# We fill it with the specified color.
image_data = np.full((height, width, 3), color, dtype=np.uint8)

# Create an image using PIL from the numpy array
image = Image.fromarray(image_data, 'RGB')

# Save the image as a BMP file
image.save('./tmp/device_independent_bitmap.bmp')