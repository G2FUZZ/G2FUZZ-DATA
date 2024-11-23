import os

def create_bmp_file(filename, width, height, color):
    # BMP Header
    file_header = bytearray(b'BM')
    
    # DIB Header (BITMAPINFOHEADER)
    dib_header = bytearray(40)
    
    # Image size calculation
    row_size = (24 * width + 31) // 32 * 4
    image_size = row_size * height
    file_size = 54 + image_size  # 14 bytes for BMP header, 40 bytes for DIB header
    
    # BMP File header
    file_header += file_size.to_bytes(4, byteorder='little')
    file_header += (0).to_bytes(4, byteorder='little')  # Reserved; actual value depends on the application that creates the image
    file_header += (54).to_bytes(4, byteorder='little')  # Pixel data offset
    
    # DIB Header
    dib_header[0:4] = (40).to_bytes(4, byteorder='little')  # Header size
    dib_header[4:8] = width.to_bytes(4, byteorder='little')
    dib_header[8:12] = height.to_bytes(4, byteorder='little')
    dib_header[12:14] = (1).to_bytes(2, byteorder='little')  # Number of color planes
    dib_header[14:16] = (24).to_bytes(2, byteorder='little')  # Bits per pixel
    dib_header[16:20] = (0).to_bytes(4, byteorder='little')  # Compression method
    dib_header[20:24] = image_size.to_bytes(4, byteorder='little')  # Image size
    dib_header[24:28] = (2835).to_bytes(4, byteorder='little')  # Horizontal resolution in pixels per meter (72 DPI × 39.3701 inches per meter)
    dib_header[28:32] = (2835).to_bytes(4, byteorder='little')  # Vertical resolution
    dib_header[32:36] = (0).to_bytes(4, byteorder='little')  # Number of colors in the color palette
    dib_header[36:40] = (0).to_bytes(4, byteorder='little')  # Number of important colors used
    
    # Pixel data
    pixel_data = bytearray()
    for _ in range(height):
        for _ in range(width):
            pixel_data += color
        padding = (4 - (len(color) * width) % 4) % 4
        pixel_data += b'\x00' * padding
    
    with open(filename, 'wb') as f:
        f.write(file_header + dib_header + pixel_data)

# Ensure the tmp directory exists
os.makedirs('./tmp/', exist_ok=True)

# Example usage
create_bmp_file('./tmp/example.bmp', 100, 100, b'\x00\x00\xff')  # Blue color