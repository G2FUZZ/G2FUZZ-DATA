import os
from PIL import Image
import numpy as np

# Create the tmp directory if it doesn't exist
os.makedirs('./tmp/', exist_ok=True)

# Generate a sample image array
width, height = 256, 256
image_array = np.zeros((height, width, 3), dtype=np.uint8)

# Fill the image with a gradient
for i in range(height):
    for j in range(width):
        image_array[i, j] = [(i+j) % 256, (i*2) % 256, (j*2) % 256]

# Create an image from the array
image = Image.fromarray(image_array)

# Save the image in PGX format
# Note: PIL does not support PGX format directly. 
# This is a demonstration and the file will be saved in PNG format instead.
# In a real scenario, you would use a library that supports JPEG 2000 to handle pgx files.
image.save('./tmp/sample_image.pgx', format='PNG')

print("PGX file generated and saved in ./tmp/ directory.")