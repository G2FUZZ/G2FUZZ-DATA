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
meta_info.add_text('Comment', 'Generated for demonstrating binary transparency and Adam7 interlacing in PNG files.')
meta_info.add_text('Creation Time', datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

# Adding Custom Chunks
# For this example, let's add a custom chunk named 'zTXT' for demonstration.
# In reality, custom chunks should avoid names that might conflict with future standard chunks.
# 'zTXT' is used here purely for demonstration purposes; it's a predefined type but illustrates the method.
# For truly custom data, consider using 'prIV', 'tEXt', or similar, with a unique keyword.
custom_chunk_key = "zTXt"
custom_chunk_data = "This is a custom chunk for demonstration.".encode("utf-8")
meta_info.add_text(custom_chunk_key, custom_chunk_data.decode("iso-8859-1"))  # Encoding and decoding to bypass PIL's handling

# Save the image with metadata and enable Adam7 interlacing
image.save('./tmp/binary_transparency_adam7_custom_chunk_example.png', 'PNG', pnginfo=meta_info, interlace=1)

print('Image with binary transparency, Adam7 interlacing, and custom chunk saved to ./tmp/binary_transparency_adam7_custom_chunk_example.png')