import numpy as np
import tifffile as tiff

# Create a random 3D array as an example image data
image_data = np.random.randint(0, 255, size=(100, 100, 3), dtype=np.uint8)

# Set the tile size for the TIFF file
tile_size = (32, 32)

# Save the image data as a TIFF file with tiled structure
tiff.imwrite('./tmp/tiled_image.tiff', image_data, tile=(tile_size))

print("TIFF file with tiled structure has been saved successfully.")