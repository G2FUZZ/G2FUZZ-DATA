import numpy as np
from PIL import Image
from tifffile import TiffWriter

# Define bit depth (e.g., 8-bit per channel)
bit_depth = 8

# Generate a random image with specified bit depth
image_data = np.random.randint(0, 2**bit_depth, size=(256, 256), dtype=np.uint8)
image = Image.fromarray(image_data)

# Save the generated image as a TIFF file with Image Editing Software Compatibility and Image Watermarking features
tags = [
    (270, 's', 48, 'Image Editing Software Compatibility: Optimized for XYZ Software'),
    (270, 's', 63, 'Image Watermarking: TIFF files can incorporate digital watermarks for copyright protection or branding purposes.')
]
with TiffWriter('./tmp/bit_depth_example_with_watermark_feature.tiff') as tif:
    tif.save(image, description='Generated TIFF with additional features', extratags=tags)