import struct

def create_bmp_file(width, height, output_file):
    header = b'BM'  # Bitmap signature
    file_size = 54 + 3 * width * height  # Total file size
    reserved = 0
    data_offset = 54  # Offset to actual image data

    # DIB Header
    dib_header_size = 40
    image_width = width
    image_height = height
    planes = 1
    bits_per_pixel = 24  # 3 bytes per pixel (RGB)
    compression = 0
    image_size = 3 * width * height
    x_pixels_per_meter = 0
    y_pixels_per_meter = 0
    total_colors = 0
    important_colors = 0

    with open(output_file, 'wb') as file:
        file.write(header)
        file.write(struct.pack('<i', file_size))
        file.write(struct.pack('<H', reserved))
        file.write(struct.pack('<H', reserved))
        file.write(struct.pack('<i', data_offset))
        file.write(struct.pack('<i', dib_header_size))
        file.write(struct.pack('<i', image_width))
        file.write(struct.pack('<i', image_height))
        file.write(struct.pack('<H', planes))
        file.write(struct.pack('<H', bits_per_pixel))
        file.write(struct.pack('<i', compression))
        file.write(struct.pack('<i', image_size))
        file.write(struct.pack('<i', x_pixels_per_meter))
        file.write(struct.pack('<i', y_pixels_per_meter))
        file.write(struct.pack('<i', total_colors))
        file.write(struct.pack('<i', important_colors))

        # Generating dummy RGB data
        for _ in range(height):
            for _ in range(width):
                file.write(struct.pack('B', 0))  # Blue
                file.write(struct.pack('B', 0))  # Green
                file.write(struct.pack('B', 0))  # Red

# Creating a BMP file with size 100x100
create_bmp_file(100, 100, './tmp/platform_independence.bmp')