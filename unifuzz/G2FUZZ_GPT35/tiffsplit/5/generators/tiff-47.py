import numpy as np
import tifffile as tiff

# Generate multiple image layers with different properties
image_layer1 = np.random.randint(0, 256, size=(256, 256), dtype=np.uint8)
image_layer2 = np.random.randint(0, 256, size=(512, 512), dtype=np.uint8)

# Create metadata information for each layer
metadata_layer1 = {
    'Author': 'John Doe',
    'Description': 'Layer 1',
    'CreationDate': '2022-01-15'
}

metadata_layer2 = {
    'Author': 'Jane Smith',
    'Description': 'Layer 2',
    'CreationDate': '2022-01-16'
}

# Save the images and metadata to a multi-layer TIFF file with different compression and resolution settings
with tiff.TiffWriter('./tmp/multi_layer_image_extended.tiff') as tif:
    tif.save(image_layer1, compression='jpeg', resolution=(300, 300), metadata=metadata_layer1)
    tif.save(image_layer2, compression='deflate', resolution=(150, 150), metadata=metadata_layer2)