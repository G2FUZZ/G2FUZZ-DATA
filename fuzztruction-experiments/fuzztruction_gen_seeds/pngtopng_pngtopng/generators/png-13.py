from PIL import Image, PngImagePlugin, ImageDraw
import os
from datetime import datetime

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Create a new image with palette mode for binary transparency
image = Image.new('P', (640, 480), color='white')

# Create a palette with 256 colors, where the first color (index 0) is transparent
palette = []
for i in range(256):
    if i == 0:
        palette.extend((255, 255, 255, 0))  # Making the first color fully transparent (RGBA)
    else:
        palette.extend((i, i, i))  # Grayscale for the rest

# Ensure the palette is the correct size (768 for RGB)
palette = palette[:768]

image.putpalette(palette)
image.info['transparency'] = 0  # Setting index 0 as the transparent color

# Draw a simple shape to demonstrate transparency
draw = ImageDraw.Draw(image)
draw.rectangle([10, 10, 200, 200], fill=1)  # Filling with index 1, which is not transparent

# Prepare metadata
meta_info = PngImagePlugin.PngInfo()
meta_info.add_text('Copyright', 'Copyright 2023 by Example')
meta_info.add_text('Comment', 'Generated for demonstrating binary transparency in PNG files.')
meta_info.add_text('Creation Time', datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

# Save the image with metadata
image.save('./tmp/binary_transparency_example.png', 'PNG', pnginfo=meta_info)

print('Image with binary transparency saved to ./tmp/binary_transparency_example.png')