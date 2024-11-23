from PIL import Image
import numpy as np
import os

# Ensure the ./tmp/ directory exists
output_dir = "./tmp/"
os.makedirs(output_dir, exist_ok=True)

# Create a sample image data for RGB
width, height = 100, 100
data_rgb = np.zeros((height, width, 3), dtype=np.uint8)
# Example: drawing a red-green gradient for RGB data
for x in range(width):
    for y in range(height):
        data_rgb[y, x] = [x*255//width, y*255//height, 0]

# Create an image from the RGB data
image_rgb = Image.fromarray(data_rgb, 'RGB')
image_rgb.save(os.path.join(output_dir, 'image_rgb.tiff'), format='TIFF', compression='tiff_deflate')

# Create a sample image data for Floating Point Data
data_fp = np.zeros((height, width), dtype=np.float32)
# Example: drawing a gradient for Floating Point Data
for x in range(width):
    for y in range(height):
        # Normalizing the gradient to be between 0 and 1
        data_fp[y, x] = (x/width)*(y/height)

# TIFF supports floating point data, but this feature is not directly exposed via Pillow's high-level API.
# We create an image from the floating point data using a workaround by converting it to bytes
# and then saving it using a format that supports floating point data (e.g., TIFF).
# Note: The 'F' mode in PIL is for 32-bit floating point pixels.

image_fp = Image.fromarray(data_fp, 'F')
image_fp.save(os.path.join(output_dir, 'image_floating_point.tiff'), format='TIFF')

# The 'image_floating_point.tiff' file now contains floating point data, 
# showcasing the flexibility of the TIFF format in storing high dynamic range (HDR) and scientific imaging data.