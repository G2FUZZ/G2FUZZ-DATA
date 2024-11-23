import struct

def create_ico_file(color_depth, file_name):
    # ICO Header
    ico_header = struct.pack('<HHH', 0, 1, 1)  # Reserved, Type, Number of Images
    
    # ICO Image Directory
    if color_depth == 1:
        image_data = b'\x01\x00\x01\x00\x01\x00\x10\x10'  # Width, Height, Color Count, Reserved, Planes, Bit Count
    elif color_depth == 4:
        image_data = b'\x01\x00\x01\x00\x10\x00\x20\x20'  # Width, Height, Color Count, Reserved, Planes, Bit Count
    elif color_depth == 8:
        image_data = b'\x01\x00\x01\x00\x20\x00\x20\x20'  # Width, Height, Color Count, Reserved, Planes, Bit Count
    elif color_depth == 32:
        image_data = b'\x01\x00\x01\x00\x20\x00\x20\x20'  # Width, Height, Color Count, Reserved, Planes, Bit Count
    
    ico_image_directory = struct.pack('<BBBBHHII', image_data[0], image_data[1], image_data[2], image_data[3],
                                      image_data[4] + image_data[5], 0, 0, len(ico_header) + len(image_data) + 40)
    
    # Write ICO file
    with open(file_name, 'wb') as f:
        f.write(ico_header)
        f.write(ico_image_directory)

# Create ICO files with different color depths
create_ico_file(1, './tmp/1bit_icon.ico')
create_ico_file(4, './tmp/4bit_icon.ico')
create_ico_file(8, './tmp/8bit_icon.ico')
create_ico_file(32, './tmp/32bit_icon.ico')