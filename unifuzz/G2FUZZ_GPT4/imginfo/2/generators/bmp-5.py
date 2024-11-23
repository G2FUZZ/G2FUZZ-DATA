import os
from PIL import Image

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Create an 8-bit BMP file with a palette
# Define the size of the image
width, height = 100, 100

# Create a new image with mode 'P' for palette-based and size 100x100
image = Image.new('P', (width, height))

# Define a simple color palette: 256 colors with a gradient from black to white
# Each entry in the palette is a (R,G,B) tuple
palette = [(i, i, i) for i in range(256)]

# Flatten the palette list into a single list expected by putpalette
flat_palette = sum(palette, ())  # This converts [(R,G,B),...] into [R,G,B,...]

# Apply the palette to the image
image.putpalette(flat_palette)

# Draw some shapes to show different colors from the palette
for i in range(0, 256, 10):
    image.paste(i, [i, 0, i+10, height])

# Save the image
image.save('./tmp/palette_example.bmp')