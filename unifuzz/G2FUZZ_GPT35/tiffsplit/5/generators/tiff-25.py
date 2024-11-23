import numpy as np
import tifffile as tf

# Create metadata with Subfile Type feature
metadata = {
    'Author': 'John Doe',
    'Copyright': '2023',
    'CreationDate': '2023-09-20',
    'Compression Options': 'Lossless',
    'Subfile Type': 'Reduced Resolution Image'  # Added Subfile Type feature
}

# Create a dummy image data
image_data = np.random.randint(0, 255, size=(100, 100), dtype=np.uint8)

# Save image with metadata
tf.imwrite('./tmp/metadata_example_with_subfile_type.tiff', image_data, metadata=metadata)