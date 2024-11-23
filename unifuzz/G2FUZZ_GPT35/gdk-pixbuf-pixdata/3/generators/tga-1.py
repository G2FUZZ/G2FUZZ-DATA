import struct

def create_tga_file(color_depth, filename):
    if color_depth not in [8, 16, 24, 32]:
        print("Invalid color depth. Supported values are 8, 16, 24, or 32.")
        return

    # Define TGA header
    header = bytearray()
    header.extend(struct.pack('B', 0))  # ID Length
    header.extend(struct.pack('B', 0))  # Color Map Type
    header.extend(struct.pack('B', 2))  # Image Type (Uncompressed TrueColor)
    header.extend(struct.pack('<H', 0))  # Color Map Specification
    header.extend(struct.pack('<H', 0))  # Color Map Origin
    header.extend(struct.pack('<H', 0))  # Color Map Length
    header.extend(struct.pack('B', 0))  # Color Map Depth
    header.extend(struct.pack('<H', 0))  # X Origin
    header.extend(struct.pack('<H', 0))  # Y Origin
    header.extend(struct.pack('<H', 64))  # Image Width
    header.extend(struct.pack('<H', 64))  # Image Height
    header.extend(struct.pack('B', color_depth))  # Image Pixel Size
    header.extend(struct.pack('B', 0))  # Image Descriptor

    # Create TGA file
    with open(filename, 'wb') as f:
        f.write(header)
        # Fill with dummy pixel data
        for _ in range(64 * 64):
            if color_depth == 8:
                f.write(struct.pack('B', 0))  # 8-bit color depth
            elif color_depth == 16:
                f.write(struct.pack('<H', 0))  # 16-bit color depth
            elif color_depth in [24, 32]:
                f.write(struct.pack('BBB', 0, 0, 0))  # 24-bit or 32-bit color depth

# Generate TGA files with different color depths
create_tga_file(8, './tmp/8bit_color_depth.tga')
create_tga_file(16, './tmp/16bit_color_depth.tga')
create_tga_file(24, './tmp/24bit_color_depth.tga')
create_tga_file(32, './tmp/32bit_color_depth.tga')