import os
from PIL import Image

# Ensure the ./tmp/ directory exists
output_dir = "./tmp/"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Create a new image with 100x100 pixels, 8-bit palette mode (supports RLE compression)
image = Image.new("P", (100, 100), color=1)

# Create a palette where the first color (index 0) is black, and the second color (index 1) is white
# The palette is a list of 768 values, 256 entries of R, G, B components
palette = [0, 0, 0, 255, 255, 255] + [0] * (256 - 2) * 3  # Two colors + padding for the rest
image.putpalette(palette)

# Draw a simple pattern to demonstrate RLE compression efficiency
# Fill half of the image with color index 1 (white)
for y in range(50):
    for x in range(100):
        image.putpixel((x, y), 1)

# The other half with color index 0 (black)
for y in range(50, 100):
    for x in range(100):
        image.putpixel((x, y), 0)

# Save the image with RLE compression
file_path = os.path.join(output_dir, "compressed_rle.bmp")
image.save(file_path, "BMP", compression="RLE")