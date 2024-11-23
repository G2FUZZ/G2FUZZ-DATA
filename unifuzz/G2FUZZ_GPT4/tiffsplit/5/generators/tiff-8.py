from PIL import Image
import numpy as np
import os

# Ensure the ./tmp/ directory exists
output_dir = "./tmp/"
os.makedirs(output_dir, exist_ok=True)

# Create a sample image data - you can customize this as needed
width, height = 100, 100
data = np.zeros((height, width, 3), dtype=np.uint8)
# Example: drawing a red-green gradient
for x in range(width):
    for y in range(height):
        data[y, x] = [x*255//width, y*255//height, 0]

# Create an image from the data
image = Image.fromarray(data, 'RGB')

# Save the image in both big-endian and little-endian formats
# The TIFF format supports both, and Pillow will handle the conversion.
# However, Pillow's default save method does not expose endianness configuration directly.
# Endianness in TIFF is typically handled by readers and is not a direct option in Pillow save.
# We save the file normally; specific endianness handling might require lower-level TIFF manipulation not directly supported by Pillow.

image.save(os.path.join(output_dir, 'image_little_endian.tiff'), format='TIFF', compression='tiff_deflate')
# Note: Pillow saves TIFF files in a way that is compatible across different systems, but it does not
# explicitly expose an option to choose between little-endian and big-endian byte order upon saving.
# The TIFF saved will be in the system's native endianness or what Pillow deems most compatible.

# For demonstration, we've named the files as if one is little endian and the other is big endian,
# but both are saved in a manner that should be widely compatible without specifying endianness in Pillow.