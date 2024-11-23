import os

# Create a directory to store the generated bmp files
os.makedirs('./tmp/', exist_ok=True)

# Function to generate a bmp file with color table
def generate_bmp_with_color_table(filename):
    # BMP file header
    bmp_header = bytearray(b'BM')
    bmp_header += (154).to_bytes(4, byteorder='little')  # File size
    bmp_header += bytes(4)
    bmp_header += (122).to_bytes(4, byteorder='little')  # Data offset

    # DIB header
    dib_header = bytearray()
    dib_header += (108).to_bytes(4, byteorder='little')  # DIB header size
    dib_header += (2).to_bytes(4, byteorder='little')  # Image width
    dib_header += (2).to_bytes(4, byteorder='little')  # Image height
    dib_header += (1).to_bytes(2, byteorder='little')  # Color planes
    dib_header += (8).to_bytes(2, byteorder='little')  # Bits per pixel
    dib_header += (3).to_bytes(4, byteorder='little')  # Compression method
    dib_header += (16).to_bytes(4, byteorder='little')  # Image size
    dib_header += (2835).to_bytes(4, byteorder='little')  # Horizontal resolution
    dib_header += (2835).to_bytes(4, byteorder='little')  # Vertical resolution
    dib_header += (0).to_bytes(4, byteorder='little')  # Colors in color table
    dib_header += (0).to_bytes(4, byteorder='little')  # Important colors

    # Color table
    color_table = bytearray()
    color_table += bytearray([255, 0, 0, 0])  # Red
    color_table += bytearray([0, 255, 0, 0])  # Green
    color_table += bytearray([0, 0, 255, 0])  # Blue

    # Image data
    image_data = bytearray()
    image_data += bytes([0, 1, 2, 1])  # Pixel data

    # Combine headers and data
    bmp_data = bmp_header + dib_header + color_table + image_data

    # Write data to file
    with open(f'./tmp/{filename}', 'wb') as f:
        f.write(bmp_data)

# Generate a bmp file with color table
generate_bmp_with_color_table('sample_with_color_table.bmp')