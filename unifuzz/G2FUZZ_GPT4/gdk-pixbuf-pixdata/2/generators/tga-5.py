import os
import struct

def create_colormap_tga():
    width, height = 100, 100  # Image dimensions
    colormap_length = 3  # Number of colors in the colormap
    header = bytearray([
        0,  # ID length
        1,  # Color map type (1 = has colormap)
        1,  # Image type (1 = colormap)
        0, 0,  # First index of colormap
        colormap_length, 0,  # Length of colormap
        24,  # Colormap entry size (24 bits per pixel)
        0, 0,  # X-origin of the image
        0, 0,  # Y-origin of the image
        width & 0xFF, (width >> 8) & 0xFF,  # Width of the image
        height & 0xFF, (height >> 8) & 0xFF,  # Height of the image
        8,  # Pixel depth (8 bits per pixel for indexed color)
        0,  # Image descriptor
    ])

    # Define a simple colormap (3 colors: red, green, blue)
    colormap = bytearray([
        0xFF, 0x00, 0x00,  # Red
        0x00, 0xFF, 0x00,  # Green
        0x00, 0x00, 0xFF,  # Blue
    ])

    # Create image data that uses colors from the colormap by index
    # For simplicity, fill the image with a repeating pattern of all defined colors
    image_data = bytearray([
        (x % colormap_length) for x in range(width * height)
    ])

    # Ensure the ./tmp/ directory exists
    os.makedirs('./tmp/', exist_ok=True)

    # Write the TGA file
    with open('./tmp/colormap_image.tga', 'wb') as file:
        file.write(header)
        file.write(colormap)
        file.write(image_data)

create_colormap_tga()