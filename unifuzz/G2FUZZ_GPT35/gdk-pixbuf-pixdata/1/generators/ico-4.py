import struct

def create_ico(color_depth, file_name):
    if color_depth == 1:
        color_palette = b'\x00\x00\x00\x00\xFF\xFF\xFF\x00'
    elif color_depth == 4:
        color_palette = b'\x00\x00\x00\x00\x80\x80\x80\x00\xC0\xC0\xC0\x00\xFF\xFF\xFF\x00'
    elif color_depth == 8:
        color_palette = b'\x00\x00\x00\x00\x00\x00\x80\x00\x00\x80\x00\x00\x80\x80\x00\x00\x80\x80\x00\x80\x80\x80\x00\x80\x80\x80\x00\xc0\xc0\xc0\x00\xff\xff\xff\x00'
    elif color_depth == 24:
        color_palette = b''
    
    ico_header = struct.pack('<HHH', 0, 1, 1)
    ico_entry = struct.pack('<BBBBHHII', 32, 32, 0, 0, 1, 0, len(color_palette) + 40, 22)
    
    with open(f'./tmp/{file_name}.ico', 'wb') as f:
        f.write(ico_header)
        f.write(ico_entry)
        f.write(color_palette)

# Create ICO files with different color depths
create_ico(1, 'monochrome_icon')
create_ico(4, '16_color_icon')
create_ico(8, '256_color_icon')
create_ico(24, 'true_color_icon')