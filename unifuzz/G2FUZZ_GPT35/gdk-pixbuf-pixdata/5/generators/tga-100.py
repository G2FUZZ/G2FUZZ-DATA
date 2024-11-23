import struct

def create_complex_tga_file(image_origin):
    # TGA header
    header = bytearray()
    header.extend(struct.pack('B', 0))  # ID length
    header.extend(struct.pack('B', 0))  # Color map type
    header.extend(struct.pack('B', 2))  # Image type (True-color image)
    header.extend(struct.pack('<H', 0))  # Color map origin
    header.extend(struct.pack('<H', 0))  # Color map length
    header.extend(struct.pack('B', 0))  # Color map entry size
    header.extend(struct.pack('<H', 0))  # X origin
    header.extend(struct.pack('<H', 0))  # Y origin
    header.extend(struct.pack('<H', 200))  # Image width
    header.extend(struct.pack('<H', 200))  # Image height
    header.extend(struct.pack('B', 24))  # Pixel depth
    header.extend(struct.pack('B', 0))  # Image descriptor

    # TGA image data
    image_data = bytearray()
    for y in range(200):
        for x in range(200):
            if (x + y) % 2 == 0:
                pixel = [255, 0, 0]  # Red pixel
            else:
                pixel = [0, 255, 0]  # Green pixel
            image_data.extend(bytearray(pixel))

    # Write to file
    with open(f'./tmp/complex_image_{image_origin}.tga', 'wb') as f:
        f.write(header)
        f.write(image_data)

# Generate complex TGA files
create_complex_tga_file('custom_image')