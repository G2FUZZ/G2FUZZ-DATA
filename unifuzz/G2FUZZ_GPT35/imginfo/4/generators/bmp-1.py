import struct

def create_bmp_file(filename):
    # File Header (54 bytes)
    file_header = b'BM'  # Signature
    file_header += struct.pack('<I', 54)  # File size
    file_header += b'\x00\x00'  # Reserved
    file_header += b'\x00\x00'  # Reserved
    file_header += struct.pack('<I', 54)  # Data offset

    with open(filename, 'wb') as f:
        f.write(file_header)

# Save generated BMP file
filename = './tmp/example.bmp'
create_bmp_file(filename)
print(f'BMP file "{filename}" generated successfully.')