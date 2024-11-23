import struct

def generate_bmp_file(file_path, width, height):
    file_size = 14 + 40 + (width * height * 3)  # File size calculation for BMP file
    header = struct.pack('<2sIHHI', b'BM', file_size, 0, 0, 54)  # BMP file header
    dib_header = struct.pack('<IIIHHIIIIII', 40, width, height, 1, 24, 0, 0, 0, 0, 0, 0)  # DIB header

    with open(file_path, 'wb') as file:
        file.write(header)
        file.write(dib_header)
        for _ in range(height):
            for _ in range(width):
                file.write(struct.pack('BBB', 255, 0, 0))  # Writing RGB values (Red) for each pixel

# Generate a BMP file with specified width and height
width = 100
height = 100
file_path = './tmp/large_bmp_file.bmp'
generate_bmp_file(file_path, width, height)