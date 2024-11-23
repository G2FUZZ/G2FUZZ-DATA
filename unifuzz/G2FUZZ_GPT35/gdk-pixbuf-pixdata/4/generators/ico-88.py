import struct

def create_ico_with_complex_features(metadata):
    # ICO file header
    ico_header = struct.pack('<HHH', 0, 1, 2)
    
    # First ICO image directory (32x32)
    image_directory_32 = struct.pack('<BBBBHHII', 32, 32, 0, 0, 1, 1, len(metadata), len(ico_header) + 16)
    
    # Second ICO image directory (64x64)
    image_directory_64 = struct.pack('<BBBBHHII', 64, 64, 0, 0, 1, 1, len(metadata), len(ico_header) + 16)
    
    # Third ICO image directory (128x128)
    image_directory_128 = struct.pack('<BBBBHHII', 128, 128, 0, 0, 1, 1, len(metadata), len(ico_header) + 16)
    
    # ICO metadata chunk
    metadata_chunk = metadata.encode('utf-8')
    
    with open('./tmp/icon_with_complex_features.ico', 'wb') as f:
        f.write(ico_header)
        f.write(image_directory_32)
        f.write(metadata_chunk)
        f.write(image_directory_64)
        f.write(metadata_chunk)
        f.write(image_directory_128)
        f.write(metadata_chunk)

metadata = "Author: John Doe\nCreation Date: 2022-10-15\nCopyright: Copyright (c) John Doe"
create_ico_with_complex_features(metadata)