import numpy as np
from PIL import Image
import os

# Create the ./tmp/ directory if it doesn't exist
if not os.path.exists('./tmp/'):
    os.makedirs('./tmp/')

# Generate an image with random pixels
width, height = 256, 256
data = np.random.rand(height, width, 3) * 255 # Generate random colors
img = Image.fromarray(data.astype('uint8')).convert('RGBA')

# Save the image with lossless compression
img.save('./tmp/lossless_compression_example.png')