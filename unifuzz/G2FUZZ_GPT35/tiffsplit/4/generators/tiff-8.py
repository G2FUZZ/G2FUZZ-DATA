import numpy as np
import tifffile as tiff

# Create a sample image
image = np.random.randint(0, 255, (256, 256), dtype=np.uint8)

# Save the image as a TIFF file with tile structure
tiff.imwrite("./tmp/tile_structure.tif", image, tile=(64, 64))

print("TIFF file with tile structure created successfully.")