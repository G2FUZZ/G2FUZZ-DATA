import struct

# Function to create an ICO file with embedded metadata and multiple images with different sizes
def create_complex_ico(file_path):
    # ICO Header
    ico_header = struct.pack('<HHH', 0, 1, 2)  # Reserved, Type, Number of images

    # Icon Directory Entries
    icon_directory_entries = [
        struct.pack('<BBBBHHII', 16, 16, 0, 0, 1, 0, 0, 22),  # Image 1: 16x16
        struct.pack('<BBBBHHII', 32, 32, 0, 0, 1, 0, 0, 70)  # Image 2: 32x32
    ]

    # Icon Image Data
    icon_image_data_16x16 = b'\x00\x00\x00\x00'  # Placeholder for 16x16 image data
    icon_image_data_32x32 = b'\x00\x00\x00\x00\x00\x00\x00\x00'  # Placeholder for 32x32 image data

    # Embed metadata (example metadata)
    metadata = b'Author: John Doe\nCreation Date: 2022-01-01\nCopyright: Copyright (c) John Doe'

    # Write ICO file
    with open(file_path, 'wb') as file:
        file.write(ico_header)
        for entry in icon_directory_entries:
            file.write(entry)
        file.write(icon_image_data_16x16)
        file.write(icon_image_data_32x32)
        file.write(metadata)

# Create ICO file with embedded metadata and multiple images with different sizes
file_path = './tmp/complex_icon.ico'
create_complex_ico(file_path)
print(f'Complex ICO file created at: {file_path}')