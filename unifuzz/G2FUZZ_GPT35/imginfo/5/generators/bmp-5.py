import numpy as np
import struct

def save_bmp_file(file_path, image_data, compression=0):
    height, width = image_data.shape[:2]
    image_data = np.flipud(image_data)  # BMP files are bottom to top

    # BMP file header
    file_size = 14 + 40 + 4 * width * height
    offset = 14 + 40
    file_header = b'BM' + struct.pack('<IHHI', file_size, 0, 0, offset)

    # BMP info header
    info_header = struct.pack('<IIIHHIIIIII', 40, width, height, 1, 32, compression, 4 * width * height, 0, 0, 0, 0)

    with open(file_path, 'wb') as file:
        file.write(file_header)
        file.write(info_header)
        
        # Write image data
        for row in image_data:
            for pixel in row:
                file.write(bytes([int(pixel[2]), int(pixel[1]), int(pixel[0]), 0]))  # BGR order

# Generate a sample image
image_data = np.zeros((100, 100, 3), dtype=np.uint8)
image_data[:, :50] = [255, 0, 0]  # Red left side
image_data[:, 50:] = [0, 0, 255]  # Blue right side

# Save uncompressed BMP file
save_bmp_file('./tmp/uncompressed.bmp', image_data, compression=0)

# Save RLE compressed BMP file
save_bmp_file('./tmp/compressed.bmp', image_data, compression=1)