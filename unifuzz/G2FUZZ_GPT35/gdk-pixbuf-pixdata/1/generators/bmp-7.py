import struct

def create_bmp_file(width, height, file_path):
    file_header = struct.pack('<2sIHHI', b'BM', 54 + width * height * 3, 0, 0, 54)
    image_data = bytearray([0, 0, 255] * width * height)

    with open(file_path, 'wb') as file:
        file.write(file_header)
        file.write(image_data)

width = 100
height = 100
file_path = './tmp/platform_compatibility.bmp'

create_bmp_file(width, height, file_path)