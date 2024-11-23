import numpy as np
import tifffile as tf

# Create metadata
metadata = {
    'Author': 'John Doe',
    'Copyright': '2023',
    'CreationDate': '2023-09-20',
    'Description': 'Example image with metadata attributes'
}

# Create a dummy image data with multiple channels
image_data = np.random.randint(0, 255, size=(100, 100, 1, 1), dtype=np.uint8)  # Dimensions: height, width, channels, frames

# Reshape the image data to have a valid shape for writing to a TIFF file
image_data = np.moveaxis(image_data, -1, 0)  # Move frames to the first dimension

# Set the tile size, compression options, and metadata for the TIFF file
tile_size = (32, 32)
compression = 'deflate'  # Change compression method to 'deflate'

# Save image with metadata, tiled structure, compression, and additional metadata
tf.imwrite('./tmp/metadata_complex_example.tiff', image_data, tile=tile_size, compress=compression, metadata=metadata)

print("TIFF file with complex metadata and file structure has been saved successfully.")