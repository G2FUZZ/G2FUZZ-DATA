import numpy as np
import tifffile as tiff
import os

# Ensure the ./tmp/ directory exists
output_dir = "./tmp/"
os.makedirs(output_dir, exist_ok=True)

# Define image dimensions
width, height = 256, 256

# Layer 1: RGBA Image
image_rgba = np.zeros((height, width, 4), dtype=np.uint8)
for x in range(width):
    for y in range(height):
        image_rgba[y, x] = [x % 256, y % 256, (x+y) % 256, 255]  # RGBA

# Layer 2: Grayscale Image as Float32
image_float = np.zeros((height, width), dtype=np.float32)
for x in range(width):
    for y in range(height):
        image_float[y, x] = np.sin(np.sqrt(x**2 + y**2))

# Layer 3: RGB Image, blending layer 1 and 2
image_rgb = np.zeros((height, width, 3), dtype=np.uint8)
for x in range(width):
    for y in range(height):
        blend_value = image_float[y, x] / np.max(image_float)
        # Simple blending example
        image_rgb[y, x] = blend_value * image_rgba[y, x, :3] + (1 - blend_value) * np.array([0, 0, 255])

# Save all layers as a multi-page TIFF
with tiff.TiffWriter(os.path.join(output_dir, 'complex_image_structure.tiff'), bigtiff=True) as tif:
    tif.save(image_rgba, description='Layer 1: RGBA Image')
    tif.save(image_float, photometric='minisblack', description='Layer 2: Grayscale Float32 Image')
    tif.save(image_rgb, description='Layer 3: RGB Blended Image')

print("TIFF file with a complex structure has been saved to ./tmp/complex_image_structure.tiff")