import numpy as np
import tifffile

# Create a multi-layer TIFF file with metadata
image_data = np.random.randint(0, 255, (3, 300, 300), dtype=np.uint8)  # Three image layers
metadata = {
    'Description': 'This TIFF file contains multiple image layers and metadata.',
    'Author': 'Your Name',
    'Date': '2022-12-31'
}

# Save the multi-layer TIFF file
tifffile.imsave('./tmp/multi_layer_image.tiff', image_data, metadata=metadata)