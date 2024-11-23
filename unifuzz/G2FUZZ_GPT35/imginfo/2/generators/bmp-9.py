import struct

def generate_bmp_file(file_path, width, height):
    # BMP Header
    file_size = 14 + 40 + (width * height * 3)  # Total file size
    bmp_header = struct.pack('<2sIHHI', b'BM', file_size, 0, 0, 54)  # BMP header structure

    # DIB Header
    dib_header = struct.pack('<IIIHHIIIIII', 40, width, height, 1, 24, 0, (width * height * 3), 0, 0, 0, 0)  # DIB header structure

    # Pixel Data (RGB)
    pixel_data = b'\x00' * (width * height * 3)

    # Write to file
    with open(file_path, 'wb') as f:
        f.write(bmp_header)
        f.write(dib_header)
        f.write(pixel_data)

# Generate BMP file with specified dimensions
width = 100
height = 100
file_path = './tmp/size_limitation.bmp'
generate_bmp_file(file_path, width, height)