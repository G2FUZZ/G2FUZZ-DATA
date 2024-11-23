import os
import struct

def create_rle_tga(width, height, color):
    """
    Creates a TGA file with RLE compression.

    :param width: The width of the image
    :param height: The height of the image
    :param color: The color of the image in RGB (tuple or list)
    """
    # Ensure the tmp directory exists
    os.makedirs('./tmp/', exist_ok=True)

    # Define the path for the new TGA file
    filepath = './tmp/rle_compressed.tga'

    # Open file to write in binary mode
    with open(filepath, 'wb') as file:
        # TGA Header
        header = [
            0,  # ID length
            0,  # Color map type
            10,  # Image type: 10 for RLE Truecolor
            0, 0, 0, 0, 0,  # Color map specification
            0, 0,  # X-origin (low-high)
            0, 0,  # Y-origin (low-high)
            width & 0xFF, (width >> 8) & 0xFF,  # Width (low-high)
            height & 0xFF, (height >> 8) & 0xFF,  # Height (low-high)
            24,  # Pixel depth
            0  # Image descriptor
        ]
        file.write(bytearray(header))

        # RLE Packet
        packet_length = width * height - 1
        packet_header = 0x80 | (packet_length & 0x7F)  # Assuming the image is small enough
        file.write(struct.pack('B', packet_header))

        # Pixel data
        bgr_color = color[::-1]  # Convert RGB to BGR
        file.write(bytearray(bgr_color))

        # Footer
        footer = bytearray([
            0, 0, 0, 0,  # Extension area offset
            0, 0, 0, 0,  # Developer directory offset
        ])
        # Append the signature, dot, and null terminator directly to the bytearray
        footer += b'TRUEVISION-XFILE' + b'.' + b'\x00'
        file.write(footer)

if __name__ == "__main__":
    create_rle_tga(100, 100, (255, 0, 0))  # Red