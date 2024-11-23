import os
import numpy as np

def create_rle_tga_image(filename, width, height, color):
    """
    Create a TGA image with RLE compression.

    Parameters:
    - filename: The name of the file to save.
    - width: The width of the image.
    - height: The height of the image.
    - color: The color of the image in RGB format (tuple).
    """

    header = bytearray([
        0,  # ID length
        0,  # Color map type
        10,  # Image type (10 for RLE truecolor)
        0, 0, 0, 0,  # Color map specification
        0,  # First entry index (low byte)
        0,  # First entry index (high byte)
        0,  # Color map length (low byte)
        0,  # Color map length (high byte)
        0,  # Color map entry size
        0, 0,  # X-origin (low and high byte)
        0, 0,  # Y-origin (low and high byte)
        width & 0xFF, (width >> 8) & 0xFF,  # Width (low and high byte)
        height & 0xFF, (height >> 8) & 0xFF,  # Height (low and high byte)
        24,  # Pixel depth
        0,  # Image descriptor
    ])

    # Ensure the output directory exists
    os.makedirs(os.path.dirname(filename), exist_ok=True)

    with open(filename, 'wb') as f:
        f.write(header)

        total_pixels = width * height
        max_packet_size = 128
        for i in range(0, total_pixels, max_packet_size):
            packet_size = min(max_packet_size, total_pixels - i)
            packet_header = 0x80 | (packet_size - 1)
            f.write(bytearray([packet_header]))
            f.write(bytearray([color[2], color[1], color[0]]))

# Example usage
create_rle_tga_image('./tmp/rle_compressed.tga', 100, 100, (255, 0, 0))  # Creating a 100x100 red image