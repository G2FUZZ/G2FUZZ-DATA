import os
import numpy as np
from PIL import Image

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Generate an image with random colors
width, height = 256, 256
data = np.random.rand(height, width, 3) * 255

# Convert the data to uint8 (8-bit unsigned integers)
img_data = data.astype(np.uint8)

# Create an image from the data
image = Image.fromarray(img_data, 'RGB')

# Save the image with Adam7 interlacing enabled
image.save('./tmp/interlaced_image.png', 'PNG', interlace=True)