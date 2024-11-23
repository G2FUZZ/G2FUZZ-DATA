import numpy as np
import tifffile as tiff

# Generate multiple image layers
image_layer1 = np.random.randint(0, 256, size=(256, 256), dtype=np.uint8)
image_layer2 = np.random.randint(0, 256, size=(256, 256), dtype=np.uint8)

# Create metadata information
metadata = {
    'Author': 'John Doe',
    'Description': 'Multi-layer TIFF file with random images',
    'CreationDate': '2022-01-15'
}

# Save the images and metadata to a multi-layer TIFF file
with tiff.TiffWriter('./tmp/multi_layer_image.tiff') as tif:
    tif.save(image_layer1, description='Layer 1')
    tif.save(image_layer2, description='Layer 2')
    tif.comment = str(metadata)