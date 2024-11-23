from PIL import Image, ImageDraw
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
# Note: The approach to defining and adding custom tags might need to be adjusted based on Pillow's version and documentation.
custom_tags = {
    65000: b"\x01"  # Simplified tag definition
}

# Attempt to save image with custom tags
try:
    # Note: The 'tiffinfo' parameter and its handling might vary. This is a simplified approach.
    custom_tag_image.save(f'{output_dir}custom_tag.tiff', tiffinfo=custom_tags)
except TypeError as e:
    print(f"An error occurred: {e}")
