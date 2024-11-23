import numpy as np
import tifffile
import os

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Define the image dimensions (e.g., a very large image)
width, height = 10000, 10000  # Adjust dimensions for your needs

# Generate a large random image (using 16-bit unsigned integers to increase file size)
image = np.random.randint(0, 65535, (height, width), dtype=np.uint16)

# Save the image as a BigTIFF file
tifffile.imwrite('./tmp/large_image.tiff', image, bigtiff=True)

print("BigTIFF image generated and saved in './tmp/large_image.tiff'")