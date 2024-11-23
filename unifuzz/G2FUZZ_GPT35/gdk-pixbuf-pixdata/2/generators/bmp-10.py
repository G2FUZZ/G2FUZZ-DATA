import numpy as np
import os

def create_bmp_file(file_name, image_data):
    signature = 0x4D42  # BM in little-endian
    file_size = 54 + len(image_data)
    reserved = 0
    data_offset = 54

    width = len(image_data[0])
    height = len(image_data)

    header = np.array([signature, file_size, reserved, data_offset, 40, width, height, 1, 24, 0, 0, 0, 0, 0, 0, 0], dtype=np.uint32)

    with open(file_name, 'wb') as bmp_file:
        header.tofile(bmp_file)
        for row in image_data:
            for pixel in row:
                bmp_file.write(bytes(pixel))

def generate_image_data(width, height):
    return np.random.randint(0, 256, (height, width, 3), dtype=np.uint8)

if not os.path.exists('./tmp/'):
    os.makedirs('./tmp/')

image_width = 100
image_height = 100

image_data = generate_image_data(image_width, image_height)

file_name = './tmp/lossless_bmp_file.bmp'
create_bmp_file(file_name, image_data)
print(f'BMP file saved as {file_name}')