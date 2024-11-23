import struct

def generate_bmp_with_palette(width, height, palette):
    file_size = 54 + len(palette) * 4 + width * height
    pixel_data_offset = 54 + len(palette) * 4

    with open('./tmp/generated.bmp', 'wb') as bmp_file:
        # BMP Header
        bmp_file.write(struct.pack('<B', 66))
        bmp_file.write(struct.pack('<B', 77))
        bmp_file.write(struct.pack('<I', file_size))
        bmp_file.write(struct.pack('<I', 0))
        bmp_file.write(struct.pack('<I', pixel_data_offset))

        # DIB Header
        bmp_file.write(struct.pack('<I', 40))
        bmp_file.write(struct.pack('<I', width))
        bmp_file.write(struct.pack('<I', height))
        bmp_file.write(struct.pack('<H', 1))
        bmp_file.write(struct.pack('<H', 32))
        bmp_file.write(struct.pack('<I', 3))  # BI_BITFIELDS
        bmp_file.write(struct.pack('<I', width * height))
        bmp_file.write(struct.pack('<I', 2835))  # horizontal resolution in pixels per meter
        bmp_file.write(struct.pack('<I', 2835))  # vertical resolution in pixels per meter
        bmp_file.write(struct.pack('<I', len(palette)))
        bmp_file.write(struct.pack('<I', 0))

        # Palette
        for color in palette:
            bmp_file.write(struct.pack('<BBBB', *color))

        # Pixel Data
        for _ in range(width * height):
            bmp_file.write(struct.pack('<B', 0))

# Example palette with 3 colors: red, green, blue
palette = [(255, 0, 0, 0), (0, 255, 0, 0), (0, 0, 255, 0)]
generate_bmp_with_palette(100, 100, palette)