import numpy as np
from PIL import Image

# Create a 2D numpy array to represent the image data
image_data = np.random.randint(0, 255, size=(256, 256), dtype=np.uint8)

# Save the image data as a TIFF file with tile structure and tile-based storage
image = Image.fromarray(image_data)
image.save('./tmp/tile_based_storage.tiff', compression='tiff_deflate', tile=(128, 128), tiffinfo={286: 1})  # Tag 286 (PlanarConfiguration) set to 1 indicates tile-based storage