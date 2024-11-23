# Define a basic .ani file structure (highly simplified for demonstration)
ani_header = bytes([
    0x52, 0x49, 0x46, 0x46,  # 'RIFF'
    0xd2, 0x00, 0x00, 0x00,  # File length - Placeholder, needs to be adjusted
    0x41, 0x43, 0x4f, 0x4e,  # 'ACON'
    # ANI HEADER (anih)
    0x61, 0x6e, 0x69, 0x68,  # 'anih'
    0x24, 0x00, 0x00, 0x00,  # Struct size
    0x24, 0x00, 0x00, 0x00,  # Frames
    0x02, 0x00, 0x00, 0x00,  # Steps
    0x27, 0x00, 0x00, 0x00,  # Width
    0x27, 0x00, 0x00, 0x00,  # Height
    0x00, 0x00, 0x00, 0x00,  # Bit count
    0x01, 0x00, 0x00, 0x00,  # Planes
    0x01, 0x00, 0x00, 0x00,  # Jif rate
    0x00, 0x00, 0x00, 0x00,  # Flags
    # LIST (fram)
    0x4c, 0x49, 0x53, 0x54,  # 'LIST'
    0xa8, 0x00, 0x00, 0x00,  # List size - Placeholder, needs to be adjusted
    0x66, 0x72, 0x61, 0x6d,  # 'fram'
    # Icon image data would go here, for each frame
    # This is a highly simplified example and does not include actual image data
    # Typically, you would need to include ICON or CURSOR data here
])

# Placeholder for actual image data
# In a real scenario, you would generate or convert image data to ICON format and include it here

# Write the ani file
ani_file_path = './tmp/basic_animation.ani'
with open(ani_file_path, 'wb') as f:
    f.write(ani_header)
    # f.write(icon_data)  # Here you would write the actual image data for each frame

print(f'Basic .ani file saved to {ani_file_path}')