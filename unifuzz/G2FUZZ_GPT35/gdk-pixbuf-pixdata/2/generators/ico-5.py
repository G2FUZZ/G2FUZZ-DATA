import struct

# Function to create ICO file with compression feature
def create_ico_with_compression():
    # ICO file header
    ico_header = struct.pack(
        '<HHH',
        0,  # Reserved (must be 0)
        1,  # Image type (1 for icon, 2 for cursor)
        1   # Number of images in the file
    )

    # ICO image entry
    image_entry = struct.pack(
        '<BBBBHHII',
        32,  # Image width
        32,  # Image height
        0,   # Number of colors in the color palette (0 means default)
        0,   # Reserved (must be 0)
        1,   # Color planes
        32,  # Bits per pixel
        0,   # Image size (will be updated later)
        22   # Image data offset (ICO header + image entry size)
    )

    # ICO image data (dummy data for demonstration)
    image_data = b'\x00' * 32 * 32 * 4

    # Update image size in the image entry
    image_entry = image_entry[:12] + struct.pack('<I', len(image_data)) + image_entry[16:]

    # Create ICO file
    with open('./tmp/compressed_icon.ico', 'wb') as file:
        file.write(ico_header)
        file.write(image_entry)
        file.write(image_data)

# Create ICO file with compression feature
create_ico_with_compression()