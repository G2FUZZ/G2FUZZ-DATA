import os
from PIL import Image
import numpy as np

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Generate a sample image data
width, height = 256, 256
data = np.zeros((height, width), dtype=np.uint16)

# Create a gradient effect for demonstration
for i in range(height):
    for j in range(width):
        data[i, j] = (i + j) % 256  # Example pattern, can be replaced with actual image data

# Convert numpy array to PIL Image
image = Image.fromarray(data)

# Save the image in PGX format
# Note: PIL does not support PGX format directly. PGX is a format used in JPEG 2000 for raw images.
# We simulate this by saving in a format that could represent raw data (e.g., TIFF) as a stand-in for demonstration.
image.save('./tmp/sample_image.tiff', format='TIFF')

# Note: To properly create and handle PGX files, a library that supports JPEG 2000 and specifically PGX format should be used.
# This example uses TIFF to demonstrate the concept of saving raw image data.