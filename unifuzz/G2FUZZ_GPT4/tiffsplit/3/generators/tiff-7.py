import numpy as np
import tifffile as tiff
import os

# Ensure the ./tmp/ directory exists
output_dir = "./tmp/"
os.makedirs(output_dir, exist_ok=True)

# Create an image with an alpha channel (RGBA)
width, height = 256, 256
# Creating an image with a gradient and full opacity in alpha channel
image = np.zeros((height, width, 4), dtype=np.uint8)
for x in range(width):
    for y in range(height):
        image[y, x] = [x % 256, y % 256, (x+y) % 256, 255]  # RGBA

# Save the image as a TIFF file with alpha channel
tiff.imwrite(os.path.join(output_dir, 'image_with_alpha.tiff'), image)

print("TIFF file with alpha channel has been saved to ./tmp/image_with_alpha.tiff")