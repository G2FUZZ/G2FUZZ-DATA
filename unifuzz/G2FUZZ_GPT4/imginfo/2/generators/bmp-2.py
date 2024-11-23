import os

def create_bmp_file(filename, width, height, color):
    # BMP file header (14 bytes)
    bmp_file_header = bytes([
        0x42, 0x4D,              # 'BM' - Windows bitmap file
        0, 0, 0, 0,              # File size in bytes - will be filled later
        0, 0,                    # Reserved
        0, 0,                    # Reserved
        54, 0, 0, 0              # Start of pixel array (54 bytes)
    ])
    
    # DIB header (BITMAPINFOHEADER) - 40 bytes
    dib_header = bytes([
        40, 0, 0, 0,             # Header size (40 bytes)
        width & 0xFF, (width >> 8) & 0xFF, 0, 0,  # Image width
        height & 0xFF, (height >> 8) & 0xFF, 0, 0, # Image height
        1, 0,                    # Number of color planes
        24, 0,                   # Bits per pixel
        0, 0, 0, 0,              # Compression (none)
        0, 0, 0, 0,              # Image size (can be 0 for uncompressed)
        0, 0, 0, 0,              # Horizontal resolution (pixels/meter) - not specified
        0, 0, 0, 0,              # Vertical resolution (pixels/meter) - not specified
        0, 0, 0, 0,              # Colors in color table (0 = all)
        0, 0, 0, 0               # Important colors (0 = all)
    ])
    
    # Pixel data - solid color
    pixels = [color for _ in range(width * height)]
    # Flatten the list and convert to bytes
    pixel_data = bytes(sum(pixels, []))
    
    # Update file size in the header
    file_size = len(bmp_file_header) + len(dib_header) + len(pixel_data)
    bmp_file_header = bytearray(bmp_file_header)
    bmp_file_header[2:6] = [file_size & 0xFF, (file_size >> 8) & 0xFF, (file_size >> 16) & 0xFF, (file_size >> 24) & 0xFF]
    
    # Write to file
    if not os.path.exists('./tmp/'):
        os.makedirs('./tmp/')
    with open(f'./tmp/{filename}', 'wb') as f:
        f.write(bmp_file_header)
        f.write(dib_header)
        f.write(pixel_data)

# Example usage
create_bmp_file('test.bmp', 100, 100, [0xFF, 0x00, 0x00])  # Red color