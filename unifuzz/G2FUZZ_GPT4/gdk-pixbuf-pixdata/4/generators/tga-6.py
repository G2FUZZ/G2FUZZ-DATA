import os
import struct

def create_tga_file(file_path):
    # Ensure ./tmp/ directory exists
    os.makedirs(os.path.dirname(file_path), exist_ok=True)

    # Open file in binary write mode
    with open(file_path, 'wb') as file:
        # TGA Header for an empty image 2x2 pixels
        header = bytearray(18)
        header[2] = 2  # Image type: uncompressed true-color image
        header[12] = 2  # Width low byte
        header[13] = 0  # Width high byte
        header[14] = 2  # Height low byte
        header[15] = 0  # Height high byte
        header[16] = 24  # Pixel depth: 24 bits

        # Image Data - 4 pixels, blue
        pixels = [0xFF, 0x00, 0x00] * 4  # Red colored pixels

        # Footer Section
        # The footer is 26 bytes long:
        # - 4 bytes for the extension area offset (0 if no extension area)
        # - 4 bytes for the developer directory offset (0 if no developer area)
        # - 16 bytes for the signature "TRUEVISION-XFILE."
        # - 1 byte ASCII character "." (already in the signature)
        # - 1 byte binary zero (end-of-string terminator for the signature)
        footer = struct.pack('<II18sB', 0, 0, b'TRUEVISION-XFILE.', 0)

        # Write the TGA file
        file.write(header)  # Write the header
        file.write(bytearray(pixels))  # Write the image data
        file.write(footer)  # Write the footer

# Specify the path of the TGA file to create
tga_file_path = './tmp/example.tga'
create_tga_file(tga_file_path)