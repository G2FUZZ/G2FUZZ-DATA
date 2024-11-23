import array
import struct

def create_complex_ico():
    # ICO Header
    ico_header = struct.pack(
        '<HHH', 0, 1, 2
    )

    # ICONDIR structures for multiple icons
    icondir_1 = struct.pack(
        '<BBHHHHII', 0, 1, 1, 64, 64, 1, 32, 0
    )
    icondir_2 = struct.pack(
        '<BBHHHHII', 0, 1, 1, 32, 32, 1, 24, 0
    )

    # ICONDIRENTRY structures for each icon
    icodirentry_1 = struct.pack(
        '<BBBBHHIIII', 64, 64, 0, 0, 1, 32, 0, 0, 0, 40
    )
    icodirentry_2 = struct.pack(
        '<BBBBHHIIII', 32, 32, 0, 0, 1, 24, 0, 0, 0, 40
    )

    # BMP Headers for each icon
    bmp_header_1 = struct.pack(
        '<IIIHHIIIIII', 40, 64, 64, 1, 32, 3, 0, 0, 0, 0, 0
    )
    bmp_header_2 = struct.pack(
        '<IIIHHIIIIII', 40, 32, 32, 1, 24, 3, 0, 0, 0, 0, 0
    )

    # Bitmap data for each icon
    bitmap_data_1 = array.array('B', [255, 0, 0, 255] * 64 * 64)  # Red color with alpha 255
    bitmap_data_2 = array.array('B', [0, 255, 0] * 32 * 32)  # Green color

    # Create ICO file with multiple icons
    with open('./tmp/complex_icon.ico', 'wb') as f:
        f.write(ico_header)
        f.write(icondir_1)
        f.write(icodirentry_1)
        f.write(bmp_header_1)
        f.write(bitmap_data_1)
        f.write(icondir_2)
        f.write(icodirentry_2)
        f.write(bmp_header_2)
        f.write(bitmap_data_2)

create_complex_ico()