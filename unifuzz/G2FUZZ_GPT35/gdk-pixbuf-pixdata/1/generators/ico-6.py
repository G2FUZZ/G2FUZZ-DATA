import struct

# Define the icon file header structure
icon_header = struct.pack(
    '<3H', 0, 1, 1
)

# Define the icon directory entry structure
icon_entry = struct.pack(
    'BBBBHHII', 32, 32, 0, 0, 1, 0, 32, 22
)

# Define the icon image data for a 32x32 pixel icon
icon_data = bytes([255] * (32 * 32 * 4))

# Combine the header, directory entry, and image data to create the ICO file content
ico_content = icon_header + icon_entry + icon_data

# Save the ICO file to disk
with open('./tmp/hotspot_icon.ico', 'wb') as f:
    f.write(ico_content)