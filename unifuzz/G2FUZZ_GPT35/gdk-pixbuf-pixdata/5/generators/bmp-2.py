import struct

def create_bmp_file(width, height, pixel_data, file_path):
    file_size = 54 + len(pixel_data)  # total file size
    pixel_array_size = len(pixel_data)
    
    # BMP header
    bmp_header = struct.pack("<ccIhhI", b'B', b'M', file_size, 0, 0, 54)
    
    # DIB header
    dib_header = struct.pack("<IiiHHIIIIII", 40, width, height, 1, 24, 0, pixel_array_size, 0, 0, 0, 0)
    
    with open(file_path, "wb") as bmp_file:
        bmp_file.write(bmp_header)
        bmp_file.write(dib_header)
        bmp_file.write(pixel_data)

# Example pixel data (red, green, blue values)
pixel_data = b'\xff\x00\x00\xff\x00\x00\xff\xff\xff\x00\x00\xff\x00'

# Create BMP file with pixel data
create_bmp_file(2, 2, pixel_data, "./tmp/image.bmp")