import numpy as np
import tifffile
import os

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Create a sample large image array (10000x10000 pixels) with random content
height, width = 10000, 10000
data = np.random.randint(0, 256, (height, width, 4), dtype=np.uint8)  # Assuming a 4-channel image for CMYK inks

# Define tile dimensions - for example, 256x256 pixels
tile_width, tile_height = 256, 256

# Ink Names for a CMYK image
inknames = 'Cyan\Magenta\Yellow\Black'

# Save the image as a tiled TIFF with Ink Names metadata
tifffile.imwrite('./tmp/tiled_image_with_inks.tiff', data,
                 tile=(tile_width, tile_height),
                 metadata={'InkNames': inknames},
                 photometric='separated')  # Corrected to 'separated' for CMYK