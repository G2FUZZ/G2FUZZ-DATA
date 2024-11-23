from PIL import Image
import numpy as np
import os

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# 1-bit Monochrome BMP
image_mono = Image.new('1', (100, 100), 0)  # Create a black and white image (1-bit)
# Draw a white square in the middle
for x in range(35, 65):
    for y in range(35, 65):
        image_mono.putpixel((x, y), 1)
image_mono.save('./tmp/monochrome.bmp')

# 24-bit True Color BMP
image_24bit = Image.new('RGB', (100, 100), 'skyblue')  # Create an RGB image
# Draw a red square in the middle
for x in range(35, 65):
    for y in range(35, 65):
        image_24bit.putpixel((x, y), (255, 0, 0))
image_24bit.save('./tmp/truecolor_24bit.bmp')

# 32-bit True Color with Alpha BMP
# Create an RGBA image
image_32bit = Image.new('RGBA', (100, 100), (0, 0, 0, 0))  # Fully transparent

# Generate a half-transparent red square
for x in range(35, 65):
    for y in range(35, 65):
        image_32bit.putpixel((x, y), (255, 0, 0, 128))  # Half-transparent red

# Add a fully opaque blue border
for x in range(100):
    for y in range(5):
        image_32bit.putpixel((x, y), (0, 0, 255, 255))  # Top border
        image_32bit.putpixel((x, 95 + y), (0, 0, 255, 255))  # Bottom border
    if x < 5 or x > 94:
        for y in range(100):
            image_32bit.putpixel((x, y), (0, 0, 255, 255))  # Left and right border

image_32bit.save('./tmp/truecolor_32bit.bmp')