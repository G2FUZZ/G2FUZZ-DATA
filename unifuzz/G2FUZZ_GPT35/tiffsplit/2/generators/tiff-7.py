import numpy as np
import tifffile as tiff

# Create sample data
data = np.random.randint(0, 255, (1024, 1024), dtype=np.uint8)

# Save the data as a TIFF file with tile structure
tiff.imsave('./tmp/tile_structure_example.tiff', data, tile=(256, 256))