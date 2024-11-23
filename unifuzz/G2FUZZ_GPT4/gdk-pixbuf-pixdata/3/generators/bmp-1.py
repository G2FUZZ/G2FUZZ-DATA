import os
from PIL import Image
import numpy as np

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Define the size of the image
width, height = 256, 256

# Generate a numpy array of random colors
data = np.random.randint(0, 256, (height, width, 3), dtype=np.uint8)

# Create an image from the numpy data array
image = Image.fromarray(data, 'RGB')

# Save the image as a BMP file
image.save('./tmp/random_image.bmp')