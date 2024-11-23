import array
import struct

def create_ico_with_mask():
    # ICO Header
    ico_header = struct.pack(
        '<HHH', 0, 1, 1
    )

    # ICONDIR structure
    icondir = struct.pack(
        '<BBHHHHII', 0, 1, 1, 64, 64, 1, 32, len(ico_header) + 16 + 40
    )

    # ICONDIRENTRY structure
    icodirentry = struct.pack(
        '<BBBBHHIIII', 64, 64, 0, 0, 1, 32, 0, 0, 0, 40
    )

    # BMP Header
    bmp_header = struct.pack(
        '<IIIHHIIIIII', 40, 64, 64, 1, 32, 3, 0, 0, 0, 0, 0
    )

    # Bitmap data
    bitmap_data = array.array('B', [255, 0, 0, 255] * 64 * 64)  # Red color with alpha 255

    # Create ICO file
    with open('./tmp/masked_icon.ico', 'wb') as f:
        f.write(ico_header)
        f.write(icondir)
        f.write(icodirentry)
        f.write(bmp_header)
        f.write(bitmap_data)

create_ico_with_mask()