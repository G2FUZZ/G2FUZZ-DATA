import numpy as np
import tifffile
import os

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Create sample large image arrays (10000x10000 pixels) with random content for 3 layers
height, width, layers = 10000, 10000, 3
data_layers = [np.random.randint(0, 256, (height, width), dtype=np.uint8) for _ in range(layers)]

# Save a multi-page TIFF
output_path = './tmp/multi_layer_tiled_image.tiff'
with tifffile.TiffWriter(output_path, bigtiff=True) as tiff_writer:
    for layer_data in data_layers:
        tiff_writer.write(data=layer_data, photometric='minisblack')

print(f"Saved multi-page TIFF to {output_path}")