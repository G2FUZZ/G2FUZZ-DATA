import numpy as np
import tifffile

# Create a TIFF file with multiple image layers and metadata
data_layer1 = np.random.randint(0, 255, size=(100, 100), dtype=np.uint8)  # Generating data for layer 1
data_layer2 = np.random.randint(0, 65535, size=(100, 100), dtype=np.uint16)  # Generating data for layer 2

with tifffile.TiffWriter('./tmp/multiple_layers.tiff') as tiff:
    tiff.save(data_layer1, metadata={'Description': 'First Image Layer'})
    tiff.save(data_layer2, metadata={'Description': 'Second Image Layer', 'Author': 'John Doe'})