import numpy as np
import tifffile as tf

# Generate multiple image layers
image_layer1 = np.random.randint(0, 255, size=(100, 100), dtype=np.uint8)
image_layer2 = np.random.randint(0, 255, size=(100, 100), dtype=np.uint8)

# Create metadata information
metadata = {
    'Author': 'John Doe',
    'Copyright': '2023',
    'CreationDate': '2023-09-20',
    'AlphaChannels': 'Supports transparency information for image compositing'
}

# Save the images and metadata to a multi-layer TIFF file
with tf.TiffWriter('./tmp/multi_layer_metadata_example_with_alpha.tiff') as tif:
    tif.save(image_layer1, description='Layer 1')
    tif.save(image_layer2, description='Layer 2')
    tif.comment = str(metadata)