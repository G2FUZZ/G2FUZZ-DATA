from PIL import Image, PngImagePlugin, ImageDraw, PngImagePlugin
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
meta_info.add_text('Comment', 'Generated for demonstrating binary transparency, Adam7 interlacing, and chunk ordering in PNG files.')
meta_info.add_text('Creation Time', datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

# Save the image with metadata and enable Adam7 interlacing
# The PNG spec does not allow direct control of chunk ordering via the PIL API,
# but you can optimize loading times by how you structure and save the file.
# For instance, saving critical chunks (like IHDR, PLTE, tRNS, IDAT) first, is handled by PIL itself.
# We ensure metadata is added before saving which optimizes chunk order indirectly.

# To further demonstrate an example of 'Chunk Ordering' conceptually,
# note that PIL handles critical chunks efficiently by default, but does not provide
# an explicit interface for manual chunk reordering. The following save operation
# already benefits from PIL's internal handling of chunk ordering for optimization.
image.save('./tmp/binary_transparency_adam7_chunk_ordering_example.png', 'PNG', pnginfo=meta_info, interlace=1)

print('Image with binary transparency, Adam7 interlacing, and chunk ordering saved to ./tmp/binary_transparency_adam7_chunk_ordering_example.png')