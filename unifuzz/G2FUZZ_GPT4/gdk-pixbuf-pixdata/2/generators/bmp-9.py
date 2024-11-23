import os

def create_bmp(filename, width, height):
    # BMP Header
    file_size = width * height * 3 + 54  # 3 bytes per pixel (RGB), +54 for header
    bmp_header = b'BM' + file_size.to_bytes(4, byteorder='little') + b'\x00\x00\x00\x00' + b'\x36\x00\x00\x00'
    
    # DIB Header
    dib_header = b'\x28\x00\x00\x00' + width.to_bytes(4, byteorder='little') + height.to_bytes(4, byteorder='little') + \
                 b'\x01\x00\x18\x00' + b'\x00\x00\x00\x00' + (width * height * 3).to_bytes(4, byteorder='little') + \
                 b'\x13\x0B\x00\x00' + b'\x13\x0B\x00\x00' + b'\x00\x00\x00\x00' + b'\x00\x00\x00\x00'
    
    # Image Data
    img_data = bytearray()
    for y in range(height):
        for x in range(width):
            img_data += bytearray([
                (x + y) % 256,  # Blue
                (x * 2) % 256,  # Green
                (y * 2) % 256,  # Red
            ])
    
    # Combine all components
    bmp_data = bmp_header + dib_header + img_data
    
    # Saving the BMP file
    if not os.path.exists(os.path.dirname(filename)):
        os.makedirs(os.path.dirname(filename))
    with open(filename, 'wb') as f:
        f.write(bmp_data)

# Specify the path and the image dimensions
path = './tmp/gradient.bmp'
create_bmp(path, 100, 100)  # Creates a 100x100 gradient BMP file