import struct

def generate_bmp_file(file_path, width, height):
    # BMP file header
    file_size = 54 + 3 * width * height
    header = b'BM' + struct.pack('<I', file_size) + b'\x00\x00\x00\x00' + struct.pack('<I', 54)
    header += struct.pack('<I', 40) + struct.pack('<I', width) + struct.pack('<I', height)
    header += b'\x01\x00\x18\x00\x00\x00\x00\x00\x00\x00\x13\x0B\x00\x00\x13\x0B\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'

    # Pixel data (dummy data)
    pixel_data = b'\xFF\x00\x00' * width * height

    with open(file_path, 'wb') as f:
        f.write(header)
        f.write(pixel_data)

# Generate a BMP file with specified width and height
width = 100
height = 100
file_path = './tmp/test.bmp'
generate_bmp_file(file_path, width, height)