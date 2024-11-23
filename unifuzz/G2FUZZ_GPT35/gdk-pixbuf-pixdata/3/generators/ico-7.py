import struct

# ICO file header structure
ico_header = struct.pack(
    '<HHH',
    0,  # Reserved, must be 0
    1,  # Type 1 for ICO files
    1   # Number of images in the file
)

# Icon directory entry structure
icon_dir_entry = struct.pack(
    '<BBBBHHIIII',
    32,  # Image width
    32,  # Image height
    0,   # Number of colors in the color palette (0 means default)
    0,   # Reserved, must be 0
    1,   # Color planes
    32,  # Bits per pixel
    1024,  # Image size in bytes
    0,    # Offset of the image data from the beginning of the file (will be calculated later)
    40,   # Size of the icon directory entry
    40    # Size of the icon image data
)

# Calculate the offset of the image data from the beginning of the file
offset = len(ico_header) + len(icon_dir_entry)
icon_dir_entry = icon_dir_entry[:28] + struct.pack('<I', offset) + icon_dir_entry[32:]

# Icon image data
icon_image_data = b'\x00' * 1024

# Combine all data into the final ICO file content
ico_data = ico_header + icon_dir_entry + icon_image_data

# Write the ICO file
with open('./tmp/icon.ico', 'wb') as f:
    f.write(ico_data)

print('ICO file generated successfully!')