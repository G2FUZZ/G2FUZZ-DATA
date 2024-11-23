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
custom_tags = {
    65000: b"\x01",  # Simplified tag definition
    # Adding tags for the Differencing Predictor
    317: 2,  # Tag for Predictor with value 2 indicating usage of differencing
}

# Attempt to save image with custom tags and Differencing Predictor
try:
    # Specify additional parameters for compression and predictor
    custom_tag_image.save(f'{output_dir}custom_tag_with_predictor.tiff', compression="tiff_lzw", tiffinfo=custom_tags, predictor=2)
except TypeError as e:
    print(f"An error occurred: {e}")