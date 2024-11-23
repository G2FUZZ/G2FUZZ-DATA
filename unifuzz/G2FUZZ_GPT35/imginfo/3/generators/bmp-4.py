import struct
import os

def bmp_header(width, height):
    return (b'BM' +
            struct.pack('<I', 54 + width * height * 3) +
            b'\x00\x00\x00\x00' +
            struct.pack('<I', 54))

def bmp_info_header(width, height):
    return (struct.pack('<I', 40) +
            struct.pack('<I', width) +
            struct.pack('<I', height) +
            b'\x01\x00' +
            b'\x18\x00' +
            b'\x00\x00\x00\x00' +
            struct.pack('<I', width * height * 3) +
            b'\x13\x0B\x00\x00' +
            b'\x13\x0B\x00\x00' +
            b'\x00\x00\x00\x00' +
            b'\x00\x00\x00\x00')

def bmp_pixel_data(width, height):
    data = bytearray()
    for y in range(height):
        for x in range(width):
            data += bytes([0, 0, 255])  # RGB values (Blue)
    return data

def write_bmp_file(filename, width, height):
    with open(filename, 'wb') as bmpfile:
        bmpfile.write(bmp_header(width, height))
        bmpfile.write(bmp_info_header(width, height))
        bmpfile.write(bmp_pixel_data(width, height))

if not os.path.exists('./tmp/'):
    os.makedirs('./tmp/')

width, height = 100, 100
filename = './tmp/compressed_bmp.bmp'
write_bmp_file(filename, width, height)
print(f'BMP file with RLE compression generated and saved as {filename}')