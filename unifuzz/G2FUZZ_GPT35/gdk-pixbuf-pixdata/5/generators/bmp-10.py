import struct

def create_bmp_file(file_path, width, height, text):
    header = b'BM'
    file_size = 54 + len(text)
    reserved = 0
    offset = 54

    info_header_size = 40
    planes = 1
    bits_per_pixel = 24
    compression = 0
    image_size = 0
    x_pixels_per_meter = 0
    y_pixels_per_meter = 0
    total_colors = 0
    important_colors = 0

    with open(file_path, 'wb') as f:
        f.write(header)
        f.write(struct.pack('<i', file_size))
        f.write(struct.pack('<H', reserved))
        f.write(struct.pack('<H', reserved))
        f.write(struct.pack('<i', offset))

        f.write(struct.pack('<i', info_header_size))
        f.write(struct.pack('<i', width))
        f.write(struct.pack('<i', height))
        f.write(struct.pack('<H', planes))
        f.write(struct.pack('<H', bits_per_pixel))
        f.write(struct.pack('<i', compression))
        f.write(struct.pack('<i', image_size))
        f.write(struct.pack('<i', x_pixels_per_meter))
        f.write(struct.pack('<i', y_pixels_per_meter))
        f.write(struct.pack('<i', total_colors))
        f.write(struct.pack('<i', important_colors))

        f.write(text.encode())

# Create BMP file with the specified text
text = "Platform Independence: BMP files can be viewed on multiple platforms due to their widespread support."
create_bmp_file('./tmp/platform_independence.bmp', 300, 100, text)