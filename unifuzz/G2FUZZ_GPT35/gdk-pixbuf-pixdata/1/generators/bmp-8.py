import os

# Function to create a bmp file with specified file size
def create_bmp_file(file_size_kb, output_file):
    # BMP file header for a simple 24-bit uncompressed BMP
    bmp_header = bytearray(b'BM')  # Signature
    bmp_header += (file_size_kb * 1024).to_bytes(4, byteorder='little')  # File size
    bmp_header += bytearray(b'\x00\x00\x00\x00')  # Reserved
    bmp_header += bytearray(b'\x36\x00\x00\x00')  # Data offset
    bmp_header += bytearray(b'\x28\x00\x00\x00')  # Info header size
    bmp_header += bytearray(b'\x02\x00\x00\x00')  # Image width
    bmp_header += bytearray(b'\x02\x00\x00\x00')  # Image height
    bmp_header += bytearray(b'\x01\x00')  # Planes
    bmp_header += bytearray(b'\x18\x00')  # Bits per pixel
    bmp_header += bytearray(b'\x00\x00\x00\x00')  # Compression
    bmp_header += bytearray(b'\x10\x00\x00\x00')  # Image size
    bmp_header += bytearray(b'\x13\x0B\x00\x00')  # X pixels per meter
    bmp_header += bytearray(b'\x13\x0B\x00\x00')  # Y pixels per meter
    bmp_header += bytearray(b'\x00\x00\x00\x00')  # Colors used
    bmp_header += bytearray(b'\x00\x00\x00\x00')  # Important colors

    with open(output_file, 'wb') as bmp_file:
        bmp_file.write(bmp_header)

# Create a bmp file with a file size of 1 MB in the ./tmp/ directory
create_bmp_file(1024, './tmp/test.bmp')