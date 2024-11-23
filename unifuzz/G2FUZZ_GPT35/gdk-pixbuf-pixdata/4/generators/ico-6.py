import struct

def create_ico_with_metadata(metadata):
    # ICO file header
    ico_header = struct.pack('<HHH', 0, 1, 1)
    
    # ICO image directory
    image_directory = struct.pack('<BBBBHHII', 32, 32, 0, 0, 1, 1, len(metadata), len(ico_header) + 16)
    
    # ICO metadata chunk
    metadata_chunk = metadata.encode('utf-8')
    
    with open('./tmp/icon_with_metadata.ico', 'wb') as f:
        f.write(ico_header)
        f.write(image_directory)
        f.write(metadata_chunk)

metadata = "Author: John Doe\nCreation Date: 2022-10-15\nCopyright: Copyright (c) John Doe"
create_ico_with_metadata(metadata)