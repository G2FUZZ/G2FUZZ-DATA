import struct

# ICO file header structure
ico_header = struct.pack(
    '<HHH',
    0,  # Reserved, must be 0
    1,  # Type 1 for ICO files
    2   # Number of images in the file
)

# Icon directory entry for first image (32x32, 24-bit color)
icon_dir_entry1 = struct.pack(
    '<BBBBHHIIII',
    32,  # Image width
    32,  # Image height
    0,   # Number of colors in the color palette (0 means default)
    0,   # Reserved, must be 0
    1,   # Color planes
    24,  # Bits per pixel (24-bit color)
    3072,  # Image size in bytes (32x32x3)
    0,    # Offset of the image data from the beginning of the file (will be calculated later)
    40,   # Size of the icon directory entry
    3072  # Size of the icon image data
)

# Icon directory entry for second image (64x64, 8-bit color)
icon_dir_entry2 = struct.pack(
    '<BBBBHHIIII',
    64,   # Image width
    64,   # Image height
    0,    # Number of colors in the color palette (0 means default)
    0,    # Reserved, must be 0
    1,    # Color planes
    8,    # Bits per pixel (8-bit color)
    4096,  # Image size in bytes (64x64)
    0,     # Offset of the image data from the beginning of the file (will be calculated later)
    40,    # Size of the icon directory entry
    4096   # Size of the icon image data
)

# Calculate the offset of the image data for the first image
offset1 = len(ico_header) + len(icon_dir_entry1) + len(icon_dir_entry2)
icon_dir_entry1 = icon_dir_entry1[:28] + struct.pack('<I', offset1) + icon_dir_entry1[32:]

# Calculate the offset of the image data for the second image
offset2 = offset1 + 3072  # Size of the first image data
icon_dir_entry2 = icon_dir_entry2[:28] + struct.pack('<I', offset2) + icon_dir_entry2[32:]

# Icon image data for the first image
icon_image_data1 = b'\x00' * 3072

# Icon image data for the second image
icon_image_data2 = b'\xFF' * 4096

# Combine all data into the final ICO file content
ico_data = ico_header + icon_dir_entry1 + icon_dir_entry2 + icon_image_data1 + icon_image_data2

# Write the ICO file
with open('./tmp/extended_icon.ico', 'wb') as f:
    f.write(ico_data)

print('Extended ICO file generated successfully!')