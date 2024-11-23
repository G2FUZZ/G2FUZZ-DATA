import numpy as np
import struct

def create_bmp(width, height, output_file):
    # BMP file header
    file_size = 14 + 40 + (width * height * 3)  # 14 bytes for file header, 40 bytes for info header
    pixel_offset = 14 + 40  # Offset where pixel data starts
    bmp_header = b'BM' + struct.pack('<IHHII', file_size, 0, 0, pixel_offset, 40)

    # BMP info header
    info_header = struct.pack('<IIIHHIIIIII', 40, width, height, 1, 24, 0, 0, 0, 0, 0, 0)

    # Generate pixel data (random pixels for demonstration)
    pixel_data = np.random.randint(0, 256, (height, width, 3), dtype=np.uint8)

    with open(output_file, 'wb') as f:
        f.write(bmp_header)
        f.write(info_header)
        f.write(pixel_data.tobytes())

# Create a BMP file with random pixel data
create_bmp(128, 128, './tmp/random_image.bmp')