import numpy as np
from PIL import Image
from tifffile import TiffWriter

# Define bit depth (e.g., 8-bit per channel)
bit_depth = 8

# Generate a random image with specified bit depth
image_data = np.random.randint(0, 2**bit_depth, size=(256, 256), dtype=np.uint8)
image = Image.fromarray(image_data)

# Save the generated image as a TIFF file with Image Editing Software Compatibility feature
tags = [
    (270, 's', 48, 'Image Editing Software Compatibility: Optimized for XYZ Software')
]
with TiffWriter('./tmp/bit_depth_example_with_feature.tiff') as tif:
    tif.save(image, description='Generated TIFF with additional feature', extratags=tags)