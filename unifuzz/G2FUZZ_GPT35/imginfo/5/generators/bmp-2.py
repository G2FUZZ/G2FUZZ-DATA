import struct

def create_bmp_file(width, height, color_depth=24, compression=0):
    file_header = b'BM'
    file_size = 14 + 40 + width * height * (color_depth // 8)
    reserved = 0
    offset = 14 + 40

    info_header_size = 40
    planes = 1
    image_size = 0
    x_pixels_per_meter = 0
    y_pixels_per_meter = 0
    colors_used = 0
    important_colors = 0

    with open(f'./tmp/generated_image_{width}x{height}.bmp', 'wb') as file:
        file.write(file_header)
        file.write(struct.pack('<I', file_size))
        file.write(struct.pack('<H', reserved))
        file.write(struct.pack('<H', reserved))
        file.write(struct.pack('<I', offset))

        file.write(struct.pack('<I', info_header_size))
        file.write(struct.pack('<I', width))
        file.write(struct.pack('<I', height))
        file.write(struct.pack('<H', planes))
        file.write(struct.pack('<H', color_depth))
        file.write(struct.pack('<I', compression))
        file.write(struct.pack('<I', image_size))
        file.write(struct.pack('<I', x_pixels_per_meter))
        file.write(struct.pack('<I', y_pixels_per_meter))
        file.write(struct.pack('<I', colors_used))
        file.write(struct.pack('<I', important_colors))

        for _ in range(height):
            for _ in range(width):
                file.write(bytes([0, 0, 255]))  # Writing Blue color to each pixel

create_bmp_file(100, 100)