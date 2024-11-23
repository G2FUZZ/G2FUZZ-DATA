import os

def create_bmp_file(filename, width, height, color):
    # BMP File Header
    file_header = bytearray([
        0x42, 0x4D,  # Signature 'BM'
        0x36, 0x28, 0x00, 0x00,  # File size (will be updated later)
        0x00, 0x00,  # Reserved
        0x00, 0x00,  # Reserved
        0x36, 0x00, 0x00, 0x00   # Offset to start of Pixel Data
    ])
    
    # DIB Header (BITMAPINFOHEADER)
    dib_header = bytearray([
        0x28, 0x00, 0x00, 0x00,  # DIB Header Size
        0x64, 0x00, 0x00, 0x00,  # Width
        0x64, 0x00, 0x00, 0x00,  # Height
        0x01, 0x00,  # Number of color planes
        0x18, 0x00,  # Bits per Pixel
        0x00, 0x00, 0x00, 0x00,  # Compression
        0x00, 0x28, 0x00, 0x00,  # Image Size (will be updated later)
        0x00, 0x00, 0x00, 0x00,  # Horizontal Resolution
        0x00, 0x00, 0x00, 0x00,  # Vertical Resolution
        0x00, 0x00, 0x00, 0x00,  # Colors in Color Table
        0x00, 0x00, 0x00, 0x00   # Important Color Count
    ])
    
    # Pixel Data
    pixels = []
    for y in range(height):
        row = []
        for x in range(width):
            row.append(color)
        # BMP rows are padded to be a multiple of 4 bytes
        while len(row) % 4 != 0:
            row.append((0, 0, 0))  # Padding bytes
        pixels.extend(row)
    
    # Flatten the pixel data
    pixel_data = bytearray()
    for pixel in pixels:
        pixel_data += bytearray(pixel)
    
    # Update file size in file header
    file_size = len(file_header) + len(dib_header) + len(pixel_data)
    file_header[2:6] = file_size.to_bytes(4, byteorder='little')
    
    # Update image size in DIB header
    dib_header[20:24] = len(pixel_data).to_bytes(4, byteorder='little')
    
    # Write to file
    with open(filename, 'wb') as bmp_file:
        bmp_file.write(file_header + dib_header + pixel_data)

# Ensure the tmp directory exists
os.makedirs('./tmp/', exist_ok=True)

# Create a BMP file
create_bmp_file('./tmp/test.bmp', 100, 100, (0, 0, 255))  # Solid blue color