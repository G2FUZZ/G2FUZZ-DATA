import struct

def create_ico_with_metadata(metadata):
    # ICO file header
    ico_header = struct.pack('<HHH', 0, 1, 1)  # Reserved, Type, Number of images

    # ICO file directory entry
    icon_entry = struct.pack('<BBBBHHII', 32, 32, 0, 0, 1, 0, len(metadata) + 1, 22)  # Width, Height, Color Count, Reserved, Planes, Bit Count, Bytes In Res, Offset

    # Write ICO file
    with open('./tmp/icon_with_metadata.ico', 'wb') as f:
        f.write(ico_header)
        f.write(icon_entry)
        f.write(metadata.encode('utf-8'))

metadata = "Author: John Doe\nCreation Date: 2022-01-01\nCopyright: Copyright © 2022"
create_ico_with_metadata(metadata)