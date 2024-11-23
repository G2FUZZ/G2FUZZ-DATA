import numpy as np
import tifffile as tiff

# Create a random 3D array as an example image data with multiple channels
image_data = np.random.randint(0, 255, size=(100, 100, 3, 4), dtype=np.uint8)  # Dimensions: height, width, channels, frames

# Reshape the image data to have a valid shape for writing to a TIFF file
image_data = np.moveaxis(image_data, -1, 0)  # Move frames to the first dimension

# Set the tile size and compression options for the TIFF file
tile_size = (32, 32)
compression = 'jpeg'

# Set metadata attributes for the TIFF file
metadata = {'Author': 'John Doe', 'Description': 'Example image with multiple channels'}

# Save the image data as a TIFF file with tiled structure, compression, and metadata
tiff.imwrite('./tmp/complex_image.tiff', image_data, tile=tile_size, compress=compression, metadata=metadata)

print("TIFF file with complex file structures has been saved successfully.")