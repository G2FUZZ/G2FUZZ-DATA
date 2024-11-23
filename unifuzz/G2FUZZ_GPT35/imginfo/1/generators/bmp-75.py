import numpy as np
import os

def generate_complex_bmp(filename, width, height, num_channels=3, compression=True):
    header_size = 54
    pixel_data = np.random.randint(0, 256, (height, width, num_channels), dtype=np.uint8)
    
    with open(filename, 'wb') as f:
        f.write(b'BM')
        f.write((header_size + width * height * num_channels).to_bytes(4, byteorder='little'))
        f.write(b'\x00\x00\x00\x00')
        f.write(header_size.to_bytes(4, byteorder='little'))
        f.write(b'\x28\x00\x00\x00')
        f.write(width.to_bytes(4, byteorder='little'))
        f.write(height.to_bytes(4, byteorder='little'))
        f.write(b'\x01\x00')
        f.write((num_channels * 8).to_bytes(2, byteorder='little'))  # Bits per pixel
        f.write(b'\x00\x00\x00\x00')
        f.write((width * height * num_channels).to_bytes(4, byteorder='little'))
        f.write(b'\x13\x0B\x00\x00')
        f.write(b'\x13\x0B\x00\x00')
        f.write(b'\x00\x00\x00\x00')
        f.write(b'\x00\x00\x00\x00')
        
        if compression:
            # Implement custom compression algorithm here
            pass
        
        for h in range(height):
            for w in range(width):
                for c in range(num_channels):
                    f.write(int(pixel_data[h][w][c]).to_bytes(1, byteorder='little'))

# Create directory if it does not exist
os.makedirs('./tmp/', exist_ok=True)

# Generate BMP file with more complex file structures
generate_complex_bmp('./tmp/complex_image.bmp', 200, 150, num_channels=4, compression=True)