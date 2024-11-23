from PIL import Image
import os

# Ensure the ./tmp/ directory exists
output_dir = './tmp/'
os.makedirs(output_dir, exist_ok=True)

# Create a 24-bit RGB image
image_24bit = Image.new('RGB', (100, 100), (255, 0, 0))  # Red, green, blue
image_24bit.save(f'{output_dir}image_24bit.png')

# Create a 32-bit RGBA image (with alpha channel)
image_32bit = Image.new('RGBA', (100, 100), (0, 255, 0, 128))  # Red, green, blue, alpha
image_32bit.save(f'{output_dir}image_32bit.png')

# Note on higher color depths:
# While PIL/Pillow does not directly support creating 48-bit or 64-bit color depth images,
# we can simulate the creation of a high dynamic range (HDR) image by saving in a format
# that supports HDR, like EXR, although this requires additional libraries like OpenEXR
# which are not as straightforward to use as PIL/Pillow. Therefore, this example focuses
# on the commonly used 24-bit and 32-bit color depths.

print("Images have been saved in the ./tmp/ directory.")