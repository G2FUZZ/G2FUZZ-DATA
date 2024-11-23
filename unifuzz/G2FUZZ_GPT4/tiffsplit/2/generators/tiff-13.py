import numpy as np
import tifffile
import os

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Create a sample large image array (10000x10000 pixels) with random content
height, width = 10000, 10000
data = np.random.randint(0, 256, (height, width), dtype=np.uint8)

# Define tile dimensions - for example, 256x256 pixels
tile_width, tile_height = 256, 256

# Save the image as a tiled TIFF
# Note: tifffile.write can automatically handle tiling if the 'tile=' parameter is provided
tifffile.imwrite('./tmp/tiled_image.tiff', data, tile=(tile_width, tile_height))