import struct

def create_ico(color_depth, file_name, image_sizes):
    if color_depth == 1:
        color_palette = b'\x00\x00\x00\x00\xFF\xFF\xFF\x00'
    elif color_depth == 4:
        color_palette = b'\x00\x00\x00\x00\x80\x80\x80\x00\xC0\xC0\xC0\x00\xFF\xFF\xFF\x00'
    elif color_depth == 8:
        color_palette = b'\x00\x00\x00\x00\x00\x00\x80\x00\x00\x80\x00\x00\x80\x80\x00\x00\x80\x80\x00\x80\x80\x80\x00\x80\x80\x80\x00\xc0\xc0\xc0\x00\xff\xff\xff\x00'
    elif color_depth == 24:
        color_palette = b''
    
    ico_header = struct.pack('<HHH', 0, 1, len(image_sizes))
    
    ico_entries = b''
    offset = 6 + len(image_sizes) * 16
    
    for size in image_sizes:
        width, height = size
        ico_entry = struct.pack('<BBBBHHII', width, height, 0, 0, 1, 0, len(color_palette) + 40, offset)
        ico_entries += ico_entry
        offset += width * height * (color_depth // 8)
    
    with open(f'./tmp/{file_name}.ico', 'wb') as f:
        f.write(ico_header)
        f.write(ico_entries)
        f.write(color_palette)

# Create ICO files with multiple image sizes and color depths
image_sizes = [(16, 16), (32, 32), (48, 48)]
create_ico(24, 'complex_icon', image_sizes)