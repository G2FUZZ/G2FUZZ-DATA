import numpy as np
import os

def generate_bmp_with_rle_compression(filename, width, height):
    header_size = 54
    pixel_data = np.random.randint(0, 256, (height, width, 3), dtype=np.uint8)
    
    with open(filename, 'wb') as f:
        f.write(b'BM')
        f.write((header_size + width * height * 3).to_bytes(4, byteorder='little'))
        f.write(b'\x00\x00\x00\x00')
        f.write(header_size.to_bytes(4, byteorder='little'))
        f.write(b'\x28\x00\x00\x00')
        f.write(width.to_bytes(4, byteorder='little'))
        f.write(height.to_bytes(4, byteorder='little'))
        f.write(b'\x01\x00')
        f.write(b'\x18\x00')
        f.write(b'\x00\x00\x00\x00')
        f.write((width * height * 3).to_bytes(4, byteorder='little'))
        f.write(b'\x13\x0B\x00\x00')
        f.write(b'\x13\x0B\x00\x00')
        f.write(b'\x00\x00\x00\x00')
        f.write(b'\x00\x00\x00\x00')
        
        for h in range(height):
            for w in range(width):
                f.write(pixel_data[h][w].tobytes())

# Create directory if it does not exist
os.makedirs('./tmp/', exist_ok=True)

# Generate BMP file with RLE compression
generate_bmp_with_rle_compression('./tmp/compressed_image.bmp', 100, 100)