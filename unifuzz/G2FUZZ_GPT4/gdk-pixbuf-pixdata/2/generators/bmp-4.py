import os
from PIL import Image

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Function to create a BMP file with a color palette
def create_bmp_with_palette(filename, size, bit_depth):
    # Create a new image with a specified bit depth
    # Mode 'P' indicates the use of a palette
    image = Image.new('P', size)

    # Define a simple color palette: 256 colors ranging from black to red, green, blue, then gradients
    palette = []
    for i in range(256):
        palette.extend((i, i//2, i//3))  # Simple gradient for demonstration
    image.putpalette(palette)

    # Draw a simple pattern to demonstrate the use of the palette
    for x in range(size[0]):
        for y in range(size[1]):
            image.putpixel((x, y), (x + y) % 256)

    # Save the image
    image.save(filename, format='BMP', bits=bit_depth)

# Example usage
create_bmp_with_palette('./tmp/palette_8bit.bmp', (256, 256), 8)