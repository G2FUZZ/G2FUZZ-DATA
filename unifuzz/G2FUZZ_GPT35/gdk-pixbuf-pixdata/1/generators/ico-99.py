import struct

def create_complex_ico_with_metadata(metadata):
    # ICO file header
    ico_header = struct.pack('<HHH', 0, 1, 2)  # Reserved, Type, Number of images

    # ICO file directory entries
    icon_entries = b''
    
    # First image entry
    icon_entry_1 = struct.pack('<BBBBHHII', 16, 16, 0, 0, 1, 4, len(metadata) + 1, 22)  # Width, Height, Color Count, Reserved, Planes, Bit Count, Bytes In Res, Offset
    icon_entries += icon_entry_1
    
    # Second image entry
    icon_entry_2 = struct.pack('<BBBBHHII', 32, 32, 0, 0, 1, 8, len(metadata) + 1, 22 + len(icon_entry_1) + len(metadata))  # Width, Height, Color Count, Reserved, Planes, Bit Count, Bytes In Res, Offset
    icon_entries += icon_entry_2

    # Write ICO file
    with open('./tmp/complex_icon_with_metadata.ico', 'wb') as f:
        f.write(ico_header)
        f.write(icon_entries)
        f.write(metadata.encode('utf-8'))

metadata = "Author: John Doe\nCreation Date: 2022-01-01\nCopyright: Copyright © 2022"
create_complex_ico_with_metadata(metadata)