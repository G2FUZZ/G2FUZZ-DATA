import struct

def create_complex_ico(metadata):
    ico_header = struct.pack('<HHH', 0, 1, 2)
    
    image_directories = [
        struct.pack('<BBBBHHII', 32, 32, 0, 0, 1, 1, len(metadata), len(ico_header) + 16),
        struct.pack('<BBBBHHII', 64, 64, 0, 0, 1, 1, len(metadata), len(ico_header) + 16),
        struct.pack('<BBBBHHII', 128, 128, 0, 0, 1, 1, len(metadata), len(ico_header) + 16),
        # Add more image directories with different sizes and properties here
    ]
    
    metadata_chunk = metadata.encode('utf-8')
    
    with open('./tmp/complex_icon.ico', 'wb') as f:
        f.write(ico_header)
        for image_directory in image_directories:
            f.write(image_directory)
            f.write(metadata_chunk)

metadata = "Author: John Doe\nCreation Date: 2022-10-15\nCopyright: Copyright (c) John Doe"
create_complex_ico(metadata)