import numpy as np
import tifffile
import os

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Define the image dimensions (e.g., a very large image)
width, height = 10000, 10000  # Adjust dimensions for your needs

# Generate a large random image (using 16-bit unsigned integers to increase file size)
# For Planar Configuration, let's create a 3-channel (RGB) image
image = np.random.randint(0, 65535, (3, height, width), dtype=np.uint16)

# Save the image as a BigTIFF file with Planar Configuration
# To specify Planar Configuration, use the 'photometric' and 'planarconfig' parameters in tifffile.imwrite()
tifffile.imwrite('./tmp/large_image_planar.tiff', image, bigtiff=True, photometric='rgb', planarconfig='separate')

print("BigTIFF image with Planar Configuration generated and saved in './tmp/large_image_planar.tiff'")