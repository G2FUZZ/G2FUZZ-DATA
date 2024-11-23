import struct

def create_tga_file(image_origin):
    # TGA header
    header = bytearray()
    header.extend(struct.pack('B', 0))  # ID length
    header.extend(struct.pack('B', 0))  # Color map type
    header.extend(struct.pack('B', 10))  # Image type (RLE compressed true-color image)
    header.extend(struct.pack('<H', 0))  # Color map origin
    header.extend(struct.pack('<H', 0))  # Color map length
    header.extend(struct.pack('B', 0))  # Color map entry size
    header.extend(struct.pack('<H', 0))  # X origin
    header.extend(struct.pack('<H', 0))  # Y origin
    header.extend(struct.pack('<H', 1))  # Image width
    header.extend(struct.pack('<H', 1))  # Image height
    header.extend(struct.pack('B', 24))  # Pixel depth
    header.extend(struct.pack('B', 0))  # Image descriptor

    # TGA image data
    image_data = bytearray([255, 0, 0])  # Red pixel

    # Write to file
    with open(f'./tmp/image_{image_origin}.tga', 'wb') as f:
        f.write(header)
        f.write(image_data)

# Generate TGA files
create_tga_file('top_down')
create_tga_file('bottom_up')