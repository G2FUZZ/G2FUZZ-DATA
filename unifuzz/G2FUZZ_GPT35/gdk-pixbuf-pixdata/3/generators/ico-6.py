import io
import struct

def create_ico_with_compression():
    # ICO file header
    ico_header = struct.pack('<HHH', 0, 1, 1)

    # ICO directory entry
    icon_dir_entry = struct.pack('<BBBBHHII', 0, 0, 1, 0, 64, 64, 0, 22)

    # ICO image data
    image_data = b'\x00' * 64 * 64 * 4

    # Create ICO file content by concatenating header, directory entry, and image data
    ico_content = ico_header + icon_dir_entry + image_data

    # Write the ICO content to a file
    with open('./tmp/compressed.ico', 'wb') as f:
        f.write(ico_content)

create_ico_with_compression()