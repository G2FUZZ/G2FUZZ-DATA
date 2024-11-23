from PIL import Image
import numpy as np
import os

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# 1-bit image (Black and White)
image_1bit = Image.new('1', (100, 100), 0)  # Creating a 100x100 black image
# Adding white pixels to make a simple pattern
for i in range(0, 100, 2):
    for j in range(0, 100, 2):
        image_1bit.putpixel((i, j), 1)
image_1bit.save('./tmp/1bit_image.png')

# 8-bit image (256 colors)
# Generating a gradient
image_8bit = Image.new('P', (256, 256))
for x in range(256):
    for y in range(256):
        image_8bit.putpixel((x, y), x % 256)
image_8bit.save('./tmp/8bit_image.png')

# 24-bit image (16.7 million colors)
# Creating a 256x256 image with a gradient showcasing potentially millions of colors
image_24bit = Image.new('RGB', (256, 256))
for x in range(256):
    for y in range(256):
        image_24bit.putpixel((x, y), (x, y, int((x+y)/2)))
image_24bit.save('./tmp/24bit_image.png')