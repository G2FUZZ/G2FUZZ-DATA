import numpy as np
from PIL import Image
import os

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Generate an image with random colors
width, height = 800, 600
image_data = np.random.rand(height, width, 3) * 255

# Convert the numpy array to an Image object
image = Image.fromarray(image_data.astype('uint8'))

# Save the image with chroma subsampling
# JPEG uses YCbCr color space, where Y is luminance, Cb and Cr are chrominance channels
# 4:2:0 subsampling averages the chrominance channels over 2x2 pixel blocks
# This reduces the color resolution but retains the luminance resolution
image.save('./tmp/chroma_subsampling_example.jpg', 'JPEG', quality=85, subsampling='4:2:0')

print('Image with chroma subsampling saved to ./tmp/chroma_subsampling_example.jpg')