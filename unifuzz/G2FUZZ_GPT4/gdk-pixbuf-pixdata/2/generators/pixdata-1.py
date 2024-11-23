import os
import numpy as np
from PIL import Image

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Creating an example image using numpy
# This will create an image of size 256x256 with random colors
image_data = np.random.rand(256, 256, 3) * 255  # Random colors
formatted_image_data = image_data.astype(np.uint8)  # Convert to unsigned byte format

# Create an image object using PIL
img = Image.fromarray(formatted_image_data)

# Save the image with compression
# For demonstration, we'll use both lossy (JPEG) and lossless (PNG) compression

# Lossy compression using JPEG
lossy_path = './tmp/lossy_compressed_image.jpg'
img.save(lossy_path, 'JPEG', quality=85)  # Adjust the quality for more or less compression

# Lossless compression using PNG
lossless_path = './tmp/lossless_compressed_image.png'
img.save(lossless_path, 'PNG', optimize=True)  # Enable optimization for some size reduction