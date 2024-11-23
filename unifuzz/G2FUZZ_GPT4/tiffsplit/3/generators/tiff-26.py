import numpy as np
from PIL import Image
import os

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Create a sample image - let's create a gradient image for demonstration
width, height = 256, 256
array = np.zeros((height, width, 3), dtype=np.uint8)

# Creating a gradient effect for demonstration purposes
for i in range(height):
    for j in range(width):
        array[i, j] = [i % 256, j % 256, (i+j) % 256]

# List of compression schemes to demonstrate
compression_schemes = ['tiff_lzw', 'jpeg', 'tiff_adobe_deflate']

# Save the same image with different compression schemes
for compression in compression_schemes:
    img = Image.fromarray(array)
    img.save(f'./tmp/sample_{compression}.tiff', compression=compression)

# Additional code for Strip and Tile Organization feature
# Define strip and tile dimensions
tile_dimensions = (128, 128)  # Example: 128x128 pixels for tiles
strip_height = 16  # Example: Each strip is 16 pixels high

# Save image with tiling
img.save('./tmp/sample_tiled.tiff', tile=tile_dimensions)

# Save image with strip organization
img.save('./tmp/sample_strip.tiff', save_all=True, append_images=[img], height=strip_height)