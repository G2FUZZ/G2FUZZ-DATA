from PIL import Image
import numpy as np
import tifffile as tiff

# Create a new RGBA image with multiple channels and frames
image_data = np.random.randint(0, 255, size=(3, 100, 100, 4), dtype=np.uint8)  # Dimensions: frames, height, width, channels

# Set the tile size and compression options for the TIFF file
tile_size = (32, 32)
compression = 'jpeg'

# Set metadata attributes for the TIFF file
metadata = {'Author': 'Alice Smith', 'Description': 'Example RGBA image with multiple channels and frames'}

# Reshape the image data to match the required format for multi-frame images
image_data = np.moveaxis(image_data, 0, -1)  # Move frames to the last dimension

# Save the image data as a TIFF file with tiled structure, compression, and metadata
tiff.imwrite('./tmp/mutated_target_image.tiff', image_data, tile=tile_size, compress=compression, metadata=metadata)

print("Mutated TIFF file with complex file structures has been saved successfully.")