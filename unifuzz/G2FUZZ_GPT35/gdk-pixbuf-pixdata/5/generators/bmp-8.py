import struct

def create_bmp_file(file_path, width, height, bit_depth):
    file_size = 54 + (width * height * bit_depth) // 8
    header = bytearray(b'BM')
    header.extend(struct.pack('<I', file_size))
    header.extend(b'\x00\x00')
    header.extend(b'\x00\x00')
    header.extend(struct.pack('<I', 54))
    header.extend(struct.pack('<I', 40))
    header.extend(struct.pack('<I', width))
    header.extend(struct.pack('<I', height))
    header.extend(b'\x01\x00')
    header.extend(struct.pack('<H', bit_depth))
    header.extend(b'\x00\x00\x00\x00')
    header.extend(struct.pack('<I', (width * height * bit_depth) // 8))
    header.extend(b'\x00\x00\x00\x00')
    header.extend(b'\x00\x00\x00\x00')
    header.extend(b'\x00\x00\x00\x00')
    header.extend(b'\x00\x00\x00\x00')
    
    with open(file_path, 'wb') as file:
        file.write(header)

# Create a BMP file with dimensions 100x100 and bit depth of 24
create_bmp_file('./tmp/test.bmp', 100, 100, 24)