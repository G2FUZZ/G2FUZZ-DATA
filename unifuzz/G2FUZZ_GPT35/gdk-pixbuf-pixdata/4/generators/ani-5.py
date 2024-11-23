import os
import array

def create_ani_file(file_path, color_depth):
    header = bytearray([0x52, 0x49, 0x46, 0x46])  # "RIFF" in ASCII
    # Add header size as 4 bytes little-endian
    header += (40).to_bytes(4, byteorder='little')
    header += bytearray([0x41, 0x4E, 0x49, 0x4D])  # "ANIM" in ASCII
    header += bytearray([0x41, 0x4E, 0x49, 0x20])  # "ANI " in ASCII

    # Add color depth as 4 bytes little-endian
    header += color_depth.to_bytes(4, byteorder='little')

    with open(file_path, 'wb') as f:
        f.write(header)

    print(f"Generated '{file_path}' with color depth: {color_depth}")

# Create a folder to store the generated files
os.makedirs('./tmp/', exist_ok=True)

# Generate ani files with different color depths
create_ani_file('./tmp/ani_color_depth_8.ani', 8)
create_ani_file('./tmp/ani_color_depth_24.ani', 24)
create_ani_file('./tmp/ani_color_depth_32.ani', 32)