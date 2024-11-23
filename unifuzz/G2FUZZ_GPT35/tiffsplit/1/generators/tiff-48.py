import numpy as np
from PIL import Image
from tifffile import TiffWriter

# Create multiple images to store in the TIFF file
image1 = np.random.randint(0, 255, size=(100, 100), dtype=np.uint8)
image2 = np.random.randint(0, 255, size=(100, 100), dtype=np.uint8)

# Define custom compression settings
compression = 'deflate'  # Change compression method to 'deflate'

# Define tiled organization settings
tile_size = (64, 64)  # Set the tile size for the TIFF file

# Save the images as TIFF with custom compression, tiled organization, and multiple layers
with TiffWriter("./tmp/more_complex_features.tiff", bigtiff=True) as tiff:
    tiff.save(image1, compress=compression, tile=tile_size, description="Layer 1")
    tiff.save(image2, compress=compression, tile=tile_size, description="Layer 2")