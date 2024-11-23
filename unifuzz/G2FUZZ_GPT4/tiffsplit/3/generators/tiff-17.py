import numpy as np
from PIL import Image
import os

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Create a sample image - let's create a gradient image for demonstration
width, height = 256, 256
array = np.zeros((height, width, 3), dtype=np.uint8)

# Creating a gradient effect for demonstration purposes
for i in range(height):
    for j in range(width):
        array[i, j] = [i % 256, j % 256, (i+j) % 256]

# List of compression schemes to demonstrate
compression_schemes = ['tiff_lzw', 'jpeg', 'tiff_adobe_deflate']

# Save the same image with different compression schemes
for compression in compression_schemes:
    img = Image.fromarray(array)
    img.save(f'./tmp/sample_{compression}.tiff', compression=compression)

# To demonstrate the Data Sample Format feature, let's create a floating point array
# Convert the existing array to float32 for demonstration
float_array = np.array(array, dtype=np.float32) / 255.0  # Normalize to 0-1 for visualization

# PIL does not support saving float images directly to TIFF with compression and sample format options
# Thus, we use tifffile or a similar library that supports advanced TIFF options.
# Installing tifffile or a similar library is required for advanced TIFF features.
import tifffile as tiff

# Save the image with a floating point data sample format
tiff.imwrite('./tmp/sample_float.tiff', float_array, compression='zlib', dtype='float32')