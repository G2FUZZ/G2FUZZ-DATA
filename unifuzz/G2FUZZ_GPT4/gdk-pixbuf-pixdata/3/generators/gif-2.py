from PIL import Image
import os

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Creating an image with 256 distinct colors
width, height = 16, 16  # 16x16 pixels = 256 pixels
image = Image.new('P', (width, height))  # 'P' mode for palette-based images

# Creating a palette with 256 colors
# This example simply fills the palette with gradients of red, green, and blue
palette = []
for i in range(256):
    palette.extend((i % 8 * 32, i % 32 * 8, i % 64 * 4))

image.putpalette(palette)

# Assigning each pixel a unique color from the palette
for y in range(height):
    for x in range(width):
        image.putpixel((x, y), (x + y * width) % 256)

# Saving the image as a GIF
image_path = './tmp/palette_limitation.gif'
image.save(image_path, 'GIF')

print(f"Generated GIF saved to {image_path}")