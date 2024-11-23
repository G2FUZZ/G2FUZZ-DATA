import struct

def create_ico_file(color_depths, output_path):
    # ICO header
    ico_header = struct.pack('<HHH', 0, 1, len(color_depths))

    # ICO directory entries
    ico_directory = b''
    offset = 6 + len(color_depths) * 16  # ICO header + directory entries

    for color_depth in color_depths:
        width, height, bpp, size = color_depth
        entry = struct.pack('<BBBBHHII', width, height, 0, 0, 1, bpp, size, offset)
        ico_directory += entry
        offset += size

    with open(output_path, 'wb') as f:
        f.write(ico_header + ico_directory)

# Define color depths: (width, height, bits per pixel, image size)
color_depths = [
    (32, 32, 32, 32*32*4),  # True Color (32-bit)
    (32, 32, 8, 32*32),      # 256 colors (8-bit)
    (32, 32, 4, 32*32//2),   # 16 colors (4-bit)
]

output_dir = './tmp/'
for i, color_depth in enumerate(color_depths):
    output_path = f'{output_dir}icon_{i}.ico'
    create_ico_file([color_depth], output_path)