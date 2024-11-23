import os

def create_bmp(filename, width, height):
    # BMP file header (14 bytes)
    file_header = bytearray([
        0x42, 0x4D,             # Signature 'BM'
        0x36, 0x28, 0x00, 0x00, # File size in bytes
        0x00, 0x00,             # Reserved
        0x00, 0x00,             # Reserved
        0x36, 0x00, 0x00, 0x00  # Start of pixel array
    ])
    
    # DIB header (BITMAPINFOHEADER, 40 bytes)
    dib_header = bytearray([
        0x28, 0x00, 0x00, 0x00, # Header size
        width & 0xFF, (width >> 8) & 0xFF, 0x00, 0x00, # Image width
        height & 0xFF, (height >> 8) & 0xFF, 0x00, 0x00, # Image height
        0x01, 0x00,             # Number of color planes
        0x18, 0x00,             # Bits per pixel (24)
        0x00, 0x00, 0x00, 0x00, # Compression (no compression)
        0x00, 0x28, 0x00, 0x00, # Image size (dummy value)
        0x13, 0x0B, 0x00, 0x00, # Horizontal resolution (2835 pixels/meter)
        0x13, 0x0B, 0x00, 0x00, # Vertical resolution (2835 pixels/meter)
        0x00, 0x00, 0x00, 0x00, # Colors in color table (0 = default)
        0x00, 0x00, 0x00, 0x00  # Important colors (0 = all)
    ])
    
    # Create pixel data: a simple vertical gradient
    pixel_data = bytearray()
    for row in range(height):
        for col in range(width):
            # Gradient from black to white
            value = int((row / height) * 255)
            pixel_data += bytearray([value, value, value])  # BGRA
        # Padding for 4-byte alignment
        while len(pixel_data) % 4 != 0:
            pixel_data += b'\x00'
    
    # Update the file size in the file header
    file_size = len(file_header) + len(dib_header) + len(pixel_data)
    file_header[2:6] = file_size.to_bytes(4, byteorder='little')
    
    # Write to file
    if not os.path.exists('./tmp/'):
        os.makedirs('./tmp/')
    with open(f'./tmp/{filename}', 'wb') as bmp_file:
        bmp_file.write(file_header)
        bmp_file.write(dib_header)
        bmp_file.write(pixel_data)

# Example usage
create_bmp('gradient.bmp', 100, 100)