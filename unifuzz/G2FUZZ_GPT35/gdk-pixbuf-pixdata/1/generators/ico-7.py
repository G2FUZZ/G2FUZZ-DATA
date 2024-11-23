import struct

def write_ico_palette_optimization(filename):
    # ICO Header
    ico_header = struct.pack('<HHH', 0, 1, 1)  # Reserved, Type, Number of Images

    # Icon Directory Entry
    icon_entry = struct.pack('<BBBBHHII', 32, 32, 0, 0, 1, 24, 32, 22)  # Width, Height, Color Count, Reserved, Planes, Bit Count, Image Size, Image Offset

    # Bitmap Info Header
    bmp_info_header = struct.pack('<IIIHHIIIIII', 40, 32, 32, 1, 24, 0, 0, 0, 0, 0, 0)  # Header Size, Width, Height, Planes, Bit Count, Compression, Image Size, X Pixels Per Meter, Y Pixels Per Meter, Colors Used, Important Colors

    # Pixel Data
    pixel_data = b'\x00\x00\xFF\x00\x00\xFF' * 16  # Blue-Green repeated 16 times

    with open(filename, 'wb') as file:
        # Write ICO Header
        file.write(ico_header)

        # Write Icon Directory Entry
        file.write(icon_entry)

        # Write Bitmap Info Header
        file.write(bmp_info_header)

        # Write Pixel Data
        file.write(pixel_data)

# Save the generated ICO file
write_ico_palette_optimization('./tmp/palette_optimization.ico')