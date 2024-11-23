import struct

def create_bmp_file(file_size, output_path):
    # BMP file header
    file_header = b'BM'  # Signature
    file_header += struct.pack('<I', file_size)  # File size
    file_header += b'\x00\x00\x00\x00'  # Reserved
    file_header += b'\x36\x00\x00\x00'  # Offset to image data

    # Image data (dummy data)
    image_data = b'\xFF\x00\x00' * (file_size - len(file_header))

    # Write to file
    with open(output_path, 'wb') as f:
        f.write(file_header + image_data)

# Generate a BMP file with a file size of 100 bytes
file_size = 100
output_path = './tmp/generated_bmp_file.bmp'
create_bmp_file(file_size, output_path)