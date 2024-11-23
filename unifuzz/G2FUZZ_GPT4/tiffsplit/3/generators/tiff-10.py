from PIL import Image

# Create a gradient image (for example, 256x256 pixels)
width, height = 256, 256
image = Image.new("RGB", (width, height))

# Generate a gradient from top to bottom
for y in range(height):
    for x in range(width):
        image.putpixel((x, y), (int(x % 256), int(y % 256), 128))

# Ensure the ./tmp/ directory exists
import os
if not os.path.exists('./tmp/'):
    os.makedirs('./tmp/')

# Save the image as a TIFF with tiling
image.save('./tmp/gradient_tile.tiff', format='TIFF', tile=('tile', 128, 128))

print("TIFF image with tiling saved to ./tmp/gradient_tile.tiff")