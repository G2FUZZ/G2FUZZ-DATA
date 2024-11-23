import struct

def create_complex_tga_file(color_depth, filename):
    if color_depth not in [8, 16, 24, 32]:
        print("Invalid color depth. Supported values are 8, 16, 24, or 32.")
        return

    # Define TGA header
    header = bytearray()
    header.extend(struct.pack('B', 0))  # ID Length
    header.extend(struct.pack('B', 1))  # Color Map Type (indexed color)
    header.extend(struct.pack('B', 10))  # Image Type (RLE compressed TrueColor)
    header.extend(struct.pack('<H', 1))  # Color Map Specification
    header.extend(struct.pack('<H', 1))  # Color Map Origin
    header.extend(struct.pack('<H', 256))  # Color Map Length
    header.extend(struct.pack('B', 24))  # Color Map Depth
    header.extend(struct.pack('<H', 0))  # X Origin
    header.extend(struct.pack('<H', 0))  # Y Origin
    header.extend(struct.pack('<H', 128))  # Image Width
    header.extend(struct.pack('<H', 128))  # Image Height
    header.extend(struct.pack('B', color_depth))  # Image Pixel Size
    header.extend(struct.pack('B', 0))  # Image Descriptor

    # Create TGA file
    with open(filename, 'wb') as f:
        f.write(header)

        # Generate color map data (for indexed color)
        for i in range(256):
            f.write(struct.pack('BBB', i, i, i))  # Grayscale color map

        # Generate image data with varying pixel values
        for y in range(128):
            for x in range(128):
                if color_depth == 8:
                    f.write(struct.pack('B', x % 256))  # 8-bit color depth
                elif color_depth == 16:
                    f.write(struct.pack('<H', (x * y) % 65536))  # 16-bit color depth
                elif color_depth in [24, 32]:
                    f.write(struct.pack('BBB', x % 256, y % 256, (x + y) % 256))  # 24-bit or 32-bit color depth

# Generate TGA file with more complex features
create_complex_tga_file(24, './tmp/complex_tga_file.tga')