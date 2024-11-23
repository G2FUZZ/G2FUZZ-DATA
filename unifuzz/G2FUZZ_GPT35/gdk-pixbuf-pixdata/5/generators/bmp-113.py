import struct

def create_bmp_file(file_path, width, height, bit_depth, colors_palette=None, compression_type=0):
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
    header.extend(struct.pack('<I', compression_type))
    header.extend(struct.pack('<I', (width * height * bit_depth) // 8))
    header.extend(b'\x00\x00\x00\x00')
    header.extend(b'\x00\x00\x00\x00')

    if colors_palette:
        color_palette_data = bytearray()
        for color in colors_palette:
            color_palette_data.extend(struct.pack('<B', color[2]))
            color_palette_data.extend(struct.pack('<B', color[1]))
            color_palette_data.extend(struct.pack('<B', color[0]))
            color_palette_data.extend(b'\x00')  # Reserved byte
        header.extend(color_palette_data)

    with open(file_path, 'wb') as file:
        file.write(header)

# Create a BMP file with dimensions 100x100, bit depth of 24, and custom colors palette
colors_palette = [(255, 0, 0), (0, 255, 0), (0, 0, 255)]  # Red, Green, Blue
create_bmp_file('./tmp/test_extended.bmp', 100, 100, 24, colors_palette, 0)