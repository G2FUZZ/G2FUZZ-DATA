import struct

# Function to create an ICO file with embedded metadata
def create_ico_with_metadata(file_path):
    # ICO Header
    ico_header = struct.pack('<HHH', 0, 1, 1)  # Reserved, Type, Number of images

    # Icon Directory Entry
    icon_directory_entry = struct.pack('<BBBBHHII', 32, 32, 0, 0, 1, 0, 0, 22)  # Width, Height, Color Count, Reserved, Planes, Bit Count, Size in Bytes, Offset

    # Icon Image Data
    icon_image_data = b'\x00\x00\x00\x00'  # Placeholder for image data

    # Embed metadata (example metadata)
    metadata = b'Author: John Doe\nCreation Date: 2022-01-01\nCopyright: Copyright (c) John Doe'

    # Write ICO file
    with open(file_path, 'wb') as file:
        file.write(ico_header)
        file.write(icon_directory_entry)
        file.write(icon_image_data)
        file.write(metadata)

# Create ICO file with embedded metadata
file_path = './tmp/icon_with_metadata.ico'
create_ico_with_metadata(file_path)
print(f'ICO file with embedded metadata created at: {file_path}')