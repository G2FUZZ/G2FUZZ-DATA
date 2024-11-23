import os
import struct

def create_tga(filename, width, height, color_depth):
    # TGA Header
    header = bytearray([
        0,  # ID length
        0,  # Color map type
        2,  # Image type: Uncompressed True-Color Image
        0, 0, 0, 0, 0,  # Color map specification
        0, 0,  # X-origin
        0, 0,  # Y-origin
        width & 0xFF, (width >> 8) & 0xFF,  # Width
        height & 0xFF, (height >> 8) & 0xFF,  # Height
        color_depth,  # Pixel depth
        0  # Image descriptor
    ])

    # Generate pixel data for different color depths
    if color_depth == 8:  # Grayscale
        pixels = bytearray([i % 256 for i in range(width * height)])
    elif color_depth == 16:
        pixels = bytearray()
        for i in range(width * height):
            # Creating a simple gradient for 16-bit
            # 5 bits for blue, 5 bits for green, 5 bits for red, 1 bit for alpha
            pixel = ((i % 32) << 10) | ((i % 64) << 5) | (i % 32)
            pixels += struct.pack('<H', pixel)  # Little endian
    elif color_depth == 24:
        pixels = bytearray()
        for i in range(width * height):
            # RGB values
            pixels += struct.pack('BBB', i % 256, (i * 2) % 256, (i * 3) % 256)
    elif color_depth == 32:
        pixels = bytearray()
        for i in range(width * height):
            # RGBA values
            pixels += struct.pack('BBBB', i % 256, (i * 2) % 256, (i * 3) % 256, 255)  # Full alpha

    with open(filename, 'wb') as f:
        f.write(header + pixels)

# Ensure the ./tmp/ directory exists
if not os.path.exists('./tmp/'):
    os.makedirs('./tmp/')

# Image specifications
width, height = 100, 100  # Example dimensions

# Create TGA files for each color depth
create_tga('./tmp/8bit_grayscale.tga', width, height, 8)
create_tga('./tmp/16bit.tga', width, height, 16)
create_tga('./tmp/24bit.tga', width, height, 24)
create_tga('./tmp/32bit.tga', width, height, 32)