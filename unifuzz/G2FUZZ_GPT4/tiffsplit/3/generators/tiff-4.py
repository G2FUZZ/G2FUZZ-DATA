from PIL import Image, ImageDraw
import numpy as np
import os

# Ensure tmp directory exists
output_dir = './tmp/'
os.makedirs(output_dir, exist_ok=True)

# Generate grayscale image
width, height = 256, 256
gray_image = Image.new('L', (width, height))  # 'L' for (8-bit pixels, black and white)
for x in range(width):
    for y in range(height):
        gray_image.putpixel((x, y), x % 256)
gray_image.save(f'{output_dir}grayscale.tiff')  # Corrected variable name here

# Generate full color image
color_image = Image.new('RGB', (width, height))  # 'RGB' for true color
draw = ImageDraw.Draw(color_image)
for x in range(width):
    for y in range(height):
        draw.point((x, y), fill=(x % 256, y % 256, (x+y) % 256))
color_image.save(f'{output_dir}full_color.tiff')

# Generate binary (black and white) image
binary_image = Image.new('1', (width, height))  # '1' for (1-bit pixels, black and white, stored with one pixel per byte)
draw = ImageDraw.Draw(binary_image)
draw.line((0, 0) + binary_image.size, fill=255)
draw.line((0, binary_image.size[1], binary_image.size[0], 0), fill=255)  # Corrected typo here
binary_image.save(f'{output_dir}binary.tiff')