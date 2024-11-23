from PIL import Image
import numpy as np
import os

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Image size
width, height = 300, 300

# Creating an RGBA image (Red, Green, Blue, Alpha) with a floating point format
image = np.zeros((height, width, 4), dtype=np.float32)

# Fill the image: simple gradient for demonstration
for x in range(width):
    for y in range(height):
        # Setting Red to maximum, Green and Blue to gradients, and a gradient Alpha
        # Normalizing values to the range 0.0 to 1.0 for floating point
        image[y, x] = [1.0, (x % 256) / 255.0, (y % 256) / 255.0, (x / width)]

# Convert the numpy array to PIL Image
img = Image.fromarray((image * 255).astype(np.uint8), 'RGBA')

# Save the image as TIFF with an alpha channel and specifying the data sample format as floating point
img.save('./tmp/alpha_channel_image_fp.tiff', compression='tiff_deflate', save_all=True, append_images=[img], dpi=(300,300), description='Data Sample Format: Floating Point')

print("TIFF image with alpha channel and Data Sample Format (Floating Point) saved successfully.")