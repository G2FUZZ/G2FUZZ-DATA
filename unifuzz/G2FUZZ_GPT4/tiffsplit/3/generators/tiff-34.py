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

# Extended part: Add New Subfile Type Tag feature
# Assuming the use of tag 254 for New Subfile Type with a hypothetical value
# For demonstration, let's use 0 for a full-resolution image, 1 for a reduced-resolution image,
# and 2 for a single page of a multi-page image.
# Note: This is a fictional example as PIL doesn't directly support custom TIFF tags in this manner,
# but it's useful for understanding how you might approach this if the library did or if you use a library that allows direct manipulation of TIFF tags.

# For this demonstration, let's save a full-resolution image
new_subfile_type_tag_value = 0  # Full-resolution image

# Unfortunately, PIL.Image does not directly support setting arbitrary TIFF tags in this manner.
# Therefore, to truly implement this feature, you might need to use a more specialized library such as libtiff or PyLibTiff
# that allows for more direct manipulation of TIFF file internals.
# Here's a placeholder save call to illustrate where you would integrate this feature if possible.
img.save('./tmp/sample_with_new_subfile_type.tiff', new_subfile_type=new_subfile_type_tag_value)

# Please note, the last img.save line is for illustrative purposes and won't work as is with PIL.Image.
# You would need to use a more advanced library or method to manipulate TIFF tags directly.