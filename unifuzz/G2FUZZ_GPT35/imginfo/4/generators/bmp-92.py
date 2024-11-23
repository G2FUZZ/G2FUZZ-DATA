import struct

def generate_advanced_bmp():
    # BMP File Header
    bf_type = b'BM'
    bf_size = 154
    bf_reserved1 = 0
    bf_reserved2 = 0
    bf_offset = 1078  # Increase offset for additional palette data

    # BMP Info Header
    bi_size = 40
    bi_width = 4
    bi_height = 4
    bi_planes = 1
    bi_bit_count = 8
    bi_compression = 0
    bi_size_image = 0
    bi_x_pels_per_meter = 0
    bi_y_pels_per_meter = 0
    bi_clr_used = 512  # Increased number of colors in the palettes
    bi_clr_important = 0

    # Color Palettes
    palettes = []
    for _ in range(2):
        palette = []
        for i in range(256):
            if _ == 0:
                palette.extend([i, 0, 0, 0])  # Red palette
            else:
                palette.extend([0, i, 0, 0])  # Green palette
        palettes.append(palette)

    # Pixel Data with variable size
    pixels = [
        0, 1, 2, 3,
        4, 5, 6, 7,
        8, 9, 10, 11,
        12, 13, 14, 15
    ]

    # Write BMP file
    with open('./tmp/advanced_bmp.bmp', 'wb') as f:
        # Write BMP File Header
        f.write(struct.pack('<2sIHHI', bf_type, bf_size, bf_reserved1, bf_reserved2, bf_offset))

        # Write BMP Info Header
        f.write(struct.pack('<IIIHHIIIIII', bi_size, bi_width, bi_height, bi_planes, bi_bit_count,
                            bi_compression, bi_size_image, bi_x_pels_per_meter, bi_y_pels_per_meter,
                            bi_clr_used, bi_clr_important))

        # Write Color Palettes
        for palette in palettes:
            for color in palette:
                f.write(struct.pack('<B', color))

        # Write Pixel Data
        for pixel in pixels:
            f.write(struct.pack('<B', pixel))

    print("Advanced BMP file with multiple color palettes and variable pixel data size generated successfully.")


generate_advanced_bmp()