import os

# Function to create a bmp file with pixel data
def create_bmp_with_pixel_data(file_path, pixel_data):
    # BMP header (14 bytes)
    bmp_header = b'BM'  # Signature
    bmp_header += (1544).to_bytes(4, byteorder='little')  # File size (arbitrary value)
    bmp_header += (0).to_bytes(4, byteorder='little')  # Reserved
    bmp_header += (54).to_bytes(4, byteorder='little')  # Pixel data offset

    # DIB header (40 bytes for simplicity, actual headers can be more complex)
    dib_header = (40).to_bytes(4, byteorder='little')  # DIB header size
    dib_header += (1).to_bytes(4, byteorder='little')  # Image width
    dib_header += (1).to_bytes(4, byteorder='little')  # Image height
    dib_header += (1).to_bytes(2, byteorder='little')  # Color planes
    dib_header += (24).to_bytes(2, byteorder='little')  # Bits per pixel
    dib_header += (0).to_bytes(4, byteorder='little')  # Compression method
    dib_header += (0).to_bytes(4, byteorder='little')  # Image size
    dib_header += (0).to_bytes(4, byteorder='little')  # Horizontal resolution
    dib_header += (0).to_bytes(4, byteorder='little')  # Vertical resolution
    dib_header += (0).to_bytes(4, byteorder='little')  # Colors in color palette
    dib_header += (0).to_bytes(4, byteorder='little')  # Important colors

    with open(file_path, 'wb') as bmp_file:
        bmp_file.write(bmp_header + dib_header + pixel_data)

# Generate pixel data (arbitrary example)
pixel_data = bytes([255, 0, 0])  # Red pixel

# Create a BMP file with the pixel data
file_path = './tmp/generated_bmp.bmp'
create_bmp_with_pixel_data(file_path, pixel_data)

print(f'BMP file with pixel data generated at: {file_path}')