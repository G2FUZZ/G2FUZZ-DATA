import os

def create_bmp(filename, width, height):
    # BMP Header (14 bytes)
    bmp_header = b'BM'  # Magic Number (2 bytes)
    file_size = width * height * 3 + 54  # File size (4 bytes)
    reserved = 0  # Unused (4 bytes)
    offset = 54  # Offset to start of pixel data (4 bytes)
    bmp_header += file_size.to_bytes(4, byteorder='little')
    bmp_header += reserved.to_bytes(4, byteorder='little')
    bmp_header += offset.to_bytes(4, byteorder='little')

    # DIB Header (40 bytes)
    dib_header = (40).to_bytes(4, byteorder='little')  # DIB Header Size (4 bytes)
    dib_header += width.to_bytes(4, byteorder='little')  # Width (4 bytes)
    dib_header += height.to_bytes(4, byteorder='little')  # Height (4 bytes)
    dib_header += (1).to_bytes(2, byteorder='little')  # Planes (2 bytes)
    dib_header += (24).to_bytes(2, byteorder='little')  # Bits per Pixel (2 bytes)
    dib_header += (0).to_bytes(4, byteorder='little')  # Compression (4 bytes)
    dib_header += (width * height * 3).to_bytes(4, byteorder='little')  # Image Size (4 bytes)
    dib_header += (0).to_bytes(4, byteorder='little')  # X Pixels Per Meter (4 bytes)
    dib_header += (0).to_bytes(4, byteorder='little')  # Y Pixels Per Meter (4 bytes)
    dib_header += (0).to_bytes(4, byteorder='little')  # Total Colors (4 bytes)
    dib_header += (0).to_bytes(4, byteorder='little')  # Important Colors (4 bytes)

    # Image Data (Pixel Array)
    image_data = bytearray()
    for y in range(height):  # Each row
        for x in range(width):  # Each column
            # Creating a simple gradient effect from blue to green
            blue = x % 256
            green = y % 256
            red = 0
            image_data += bytes([blue, green, red])
    
    # Write the BMP file
    with open(filename, 'wb') as f:
        f.write(bmp_header + dib_header + image_data)

# Ensure the tmp directory exists
os.makedirs('./tmp/', exist_ok=True)

# Create a BMP file
create_bmp('./tmp/test_image.bmp', 256, 256)