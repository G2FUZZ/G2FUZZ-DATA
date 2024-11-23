import struct

def write_bmp_file(file_path, width, height):
    # BMP header
    file_header = b'BM'
    file_size = 14 + 40 + width * height * 3
    reserved = 0
    data_offset = 14 + 40

    # DIB header
    dib_header_size = 40
    image_width = width
    image_height = height
    planes = 1
    bits_per_pixel = 24
    compression = 0
    image_size = 0
    x_pixels_per_meter = 0
    y_pixels_per_meter = 0
    total_colors = 0
    important_colors = 0

    with open(file_path, 'wb') as f:
        # Write BMP header
        f.write(file_header)
        f.write(struct.pack('<I', file_size))
        f.write(struct.pack('<H', reserved))
        f.write(struct.pack('<H', reserved))
        f.write(struct.pack('<I', data_offset))

        # Write DIB header
        f.write(struct.pack('<I', dib_header_size))
        f.write(struct.pack('<I', image_width))
        f.write(struct.pack('<I', image_height))
        f.write(struct.pack('<H', planes))
        f.write(struct.pack('<H', bits_per_pixel))
        f.write(struct.pack('<I', compression))
        f.write(struct.pack('<I', image_size))
        f.write(struct.pack('<I', x_pixels_per_meter))
        f.write(struct.pack('<I', y_pixels_per_meter))
        f.write(struct.pack('<I', total_colors))
        f.write(struct.pack('<I', important_colors))

        # Write pixel data
        for y in range(height):
            for x in range(width):
                f.write(struct.pack('B', 0))  # Blue
                f.write(struct.pack('B', 0))  # Green
                f.write(struct.pack('B', 255))  # Red

# Generate and save BMP files
import os

if not os.path.exists('./tmp'):
    os.makedirs('./tmp')

write_bmp_file('./tmp/test.bmp', 100, 100)
write_bmp_file('./tmp/test2.bmp', 200, 200)