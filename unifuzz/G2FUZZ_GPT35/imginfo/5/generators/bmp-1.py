import struct

def create_bmp_file(file_name):
    # BMP file header (14 bytes)
    file_header = b'BM'  # File type
    file_header += struct.pack('<I', 26)  # File size
    file_header += struct.pack('<H', 0)  # Reserved1
    file_header += struct.pack('<H', 0)  # Reserved2
    file_header += struct.pack('<I', 26)  # Pixel data offset

    # Create the BMP file
    with open(file_name, 'wb') as bmp_file:
        bmp_file.write(file_header)
        # Write pixel data here if needed

# Save generated BMP files in ./tmp/
file_name = './tmp/sample.bmp'
create_bmp_file(file_name)