import os
from PIL import Image

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Image dimensions
width, height = 256, 256

# Create a new 8-bit image with a custom palette
image = Image.new('P', (width, height))

# Define a simple color palette: each entry consists of 3 bytes for RGB
# This example palette will just be a gradient of 256 colors
palette = []
for i in range(256):
    palette.extend((i, 255-i, i//2))  # Example gradient: varies R and G, B is a half of R

image.putpalette(palette)

# Draw some patterns to demonstrate the use of the palette
for y in range(height):
    for x in range(width):
        # Simple pattern: stripes of varying colors
        image.putpixel((x, y), (x + y) % 256)

# Save the image
image.save('./tmp/palette_example.bmp')