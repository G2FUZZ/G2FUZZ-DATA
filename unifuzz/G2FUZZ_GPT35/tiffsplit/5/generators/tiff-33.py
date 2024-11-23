import numpy as np
import tifffile as tf

# Create metadata with additional complex features
metadata = {
    'Author': 'Jane Smith',
    'Copyright': '2023',
    'CreationDate': '2023-09-20',
    'Compression Options': 'LZW',
    'Subfile Type': 'Multi-page Document',
    'Resolution Unit': 'inch',
    'X Resolution': 300,
    'Y Resolution': 300,
    'Software': 'Python Imaging Library',
    'Tiled': True,  # Added Tiled storage feature
    'Tile Width': 64,
    'Tile Length': 64,
    'Image Description': 'This tiff file contains multiple layers and is tiled.'
}

# Create dummy image data for multiple layers
num_layers = 3
image_data = [np.random.randint(0, 255, size=(100, 100), dtype=np.uint8) for _ in range(num_layers)]

# Save multi-layer image with metadata
tf.imwrite('./tmp/multi_layer_tiled_image.tiff', image_data, metadata=metadata)