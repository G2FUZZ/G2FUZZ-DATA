import numpy as np
from PIL import Image
import tifffile as tiff

# Create multiple image layers
num_layers = 3
image_layers = []
for _ in range(num_layers):
    layer = Image.new('RGB', (200, 200), (np.random.randint(0, 256), np.random.randint(0, 256), np.random.randint(0, 256)))
    image_layers.append(np.array(layer))

# Create metadata information
metadata = {
    'Author': 'Jane Smith',
    'Description': 'Multi-layer TIFF file with random layers',
    'CreationDate': '2022-01-20'
}

# Save the image layers and metadata to a multi-layer TIFF file
with tiff.TiffWriter('./tmp/multi_layer_image.tiff') as tif:
    for i, layer in enumerate(image_layers, 1):
        tif.save(layer, description=f'Layer {i}')
    tif.comment = str(metadata)