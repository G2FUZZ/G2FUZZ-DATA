from PIL import Image, ImageDraw, TiffImagePlugin
import os

# Ensure tmp directory exists
output_dir = './tmp/'
os.makedirs(output_dir, exist_ok=True)

# Generate an image with custom tags
width, height = 256, 256
custom_tag_image = Image.new('RGB', (width, height))
draw = ImageDraw.Draw(custom_tag_image)
for x in range(width):
    for y in range(height):
        draw.point((x, y), fill=(int(0.5*x) % 256, int(0.5*y) % 256, (x+y) % 256))

# Define custom tags
custom_tags = {
    65000: b"\x01",  # Simplified tag definition
    # Add Orientation Tag - Tag number 274 (0x0112) represents the Orientation
    # The value for Orientation can be from 1 to 8, where 1 is the normal orientation
    # Here, we use 1 as an example, which means the image is in its normal orientation.
    274: (1,)  # Use the numerical tag value directly
}

# Prepare to save image with custom tags
# TIFF tags must be passed in IFD format to the save function
ifd = TiffImagePlugin.ImageFileDirectory_v2()

# Add custom tags to IFD
for tag, value in custom_tags.items():
    ifd[tag] = value

# Attempt to save image with custom tags, including the Orientation Tag
try:
    custom_tag_image.save(f'{output_dir}custom_tag_with_orientation.tiff', tiffinfo=ifd)
except Exception as e:
    print(f"An error occurred: {e}")