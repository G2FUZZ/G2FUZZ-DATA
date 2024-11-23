import numpy as np
from PIL import Image
import os

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Create an example image using numpy
image_data = np.random.randint(0, 256, (100, 100, 3), dtype=np.uint8)

# Create and save the TIFF file with LZW compression
image = Image.fromarray(image_data)
image.save('./tmp/example_lzw.tiff', compression='tiff_lzw')

# Create and save the TIFF file with ZIP (Deflate) compression
image.save('./tmp/example_zip.tiff', compression='tiff_deflate')

# Create and save the TIFF file with PackBits compression
image.save('./tmp/example_packbits.tiff', compression='tiff_packbits')