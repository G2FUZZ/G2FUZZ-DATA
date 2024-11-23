import struct

# Function to create ICO file header
def create_ico_header(num_icons):
    ico_header = bytearray()
    ico_header += struct.pack('<H', 0)  # Reserved
    ico_header += struct.pack('<H', 1)  # Type (1 for ICO)
    ico_header += struct.pack('<H', num_icons)  # Number of icons
    return ico_header

# Function to create ICON directory entry
def create_icon_entry(width, height, color_count, image_size, offset):
    icon_entry = bytearray()
    icon_entry += struct.pack('B', width)  # Image width
    icon_entry += struct.pack('B', height)  # Image height
    icon_entry += struct.pack('B', color_count)  # Color count
    icon_entry += struct.pack('B', 0)  # Reserved
    icon_entry += struct.pack('<H', 1)  # Color planes
    icon_entry += struct.pack('<H', 32)  # Bits per pixel
    icon_entry += struct.pack('<I', image_size)  # Image size
    icon_entry += struct.pack('<I', offset)  # Image offset
    return icon_entry

# Create ICO file
num_icons = 1
icon_data = b'\x00\x00\x00\x00'  # Sample icon data (4 bytes)
icon_size = len(icon_data)
icon_entry = create_icon_entry(64, 64, 0, icon_size, 22)
ico_header = create_ico_header(num_icons)

with open('./tmp/icon.ico', 'wb') as file:
    file.write(ico_header)
    file.write(icon_entry)
    file.write(icon_data)