import struct

def generate_complex_bmp_file(file_path, width, height, bit_depth=24):
    # BMP file header
    file_size = 54 + (bit_depth // 8) * width * height
    header = b'BM' + struct.pack('<I', file_size) + b'\x00\x00\x00\x00' + struct.pack('<I', 54)
    header += struct.pack('<I', 108)  # Use BITMAPINFOHEADER (size=108) for color palette
    header += struct.pack('<I', width) + struct.pack('<I', height)
    header += b'\x01\x00' + struct.pack('<H', bit_depth) + b'\x00\x00\x00\x00\x00\x00\x00\x00'
    header += struct.pack('<I', 0) * 6  # Color palette info

    # Pixel data (dummy data)
    if bit_depth == 24:
        pixel_data = b'\xFF\x00\x00' * width * height
    elif bit_depth == 8:
        pixel_data = b'\x01' * width * height
    elif bit_depth == 4:
        pixel_data = b'\x0F' * (width * height // 2)
    else:
        # For other bit depths, dummy data with 0s
        pixel_data = b'\x00' * (bit_depth // 8) * width * height

    with open(file_path, 'wb') as f:
        f.write(header)
        f.write(pixel_data)

# Generate a BMP file with specified width, height, and bit depth
width = 100
height = 100
bit_depth = 8  # Use 8-bit color depth
file_path = './tmp/complex_test.bmp'
generate_complex_bmp_file(file_path, width, height, bit_depth)