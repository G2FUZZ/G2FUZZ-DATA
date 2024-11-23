import struct

def create_tga_file(filename, width, height, data):
    header = bytearray([0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, width % 256, width // 256, height % 256, height // 256, 24, 32])
    
    with open(filename, 'wb') as f:
        f.write(header)
        f.write(data)

width = 100
height = 100
data = bytearray([255, 0, 0] * width * height)  # Red image

create_tga_file('./tmp/extension_example.tga', width, height, data)