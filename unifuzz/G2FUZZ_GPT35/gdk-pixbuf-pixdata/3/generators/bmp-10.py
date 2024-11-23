import struct

def create_bmp_file(file_path, width, height):
    pixel_data = bytearray()
    
    # Creating a simple white image
    for _ in range(width * height):
        pixel_data.extend([255, 255, 255])  # White pixel
    
    file_size = 14 + 40 + (width * height * 3)  # BMP File header + DIB header + pixel data
    pixel_array_offset = 14 + 40  # BMP File header + DIB header
    
    # BMP File Header (14 bytes)
    bmp_file_header = struct.pack('<ccIHHI', b'B', b'M', file_size, 0, 0, pixel_array_offset)
    
    # DIB Header (Windows BITMAPINFOHEADER) (40 bytes)
    dib_header = struct.pack('<IIIHHIIIIII', 40, width, height, 1, 24, 0, (width * height * 3), 0, 0, 0, 0)
    
    with open(file_path, 'wb') as file:
        file.write(bmp_file_header)
        file.write(dib_header)
        file.write(pixel_data)

# Create a 100x100 white BMP file with little-endian byte order
create_bmp_file('./tmp/test.bmp', 100, 100)