from PIL import Image
import numpy as np
import os
from itertools import chain

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Color depth and corresponding mode mapping
color_depths = {
    1: '1',  # 1 bit per pixel, monochrome image
    8: 'P',  # 8 bits per pixel, paletted image
    24: 'RGB',  # 24 bits per pixel, true color image
    32: 'RGBA'  # 32 bits per pixel, true color image with alpha channel
}

# Sample sizes and color data
width, height = 100, 100  # Width and height of the image
colors = {
    1: [(0, 0, 0), (255, 255, 255)],  # Black and White for 1-bit
    8: [(i, i, i) for i in range(256)],  # Grayscale for 8-bit
    24: [(255, 0, 0), (0, 255, 0), (0, 0, 255)],  # RGB for 24-bit
    32: [(255, 0, 0, 127), (0, 255, 0, 127), (0, 0, 255, 127)]  # RGBA with half transparency for 32-bit
}

for depth, mode in color_depths.items():
    img = Image.new(mode, (width, height))

    # For 1 and 8 bits, we use a palette
    if depth == 8:
        # Flatten the color tuples list and apply as a palette
        flat_palette = list(chain.from_iterable(colors[depth]))
        img.putpalette(flat_palette)
        # Fill the image with a gradient or pattern
        for y in range(height):
            for x in range(width):
                img.putpixel((x, y), x % 256)
    elif depth == 1:
        # For 1-bit images, directly draw with black and white
        for y in range(height):
            for x in range(width):
                img.putpixel((x, y), x % 2)
    # For 24 and 32 bits, directly draw with colors
    else:
        pixels = img.load()
        for y in range(height):
            for x in range(width):
                color_index = (x // 33) % len(colors[depth])  # Simple pattern based on position
                pixels[x, y] = colors[depth][color_index]

    # Save the image in PNG format
    img.save(f'./tmp/sample_{depth}bit.png')