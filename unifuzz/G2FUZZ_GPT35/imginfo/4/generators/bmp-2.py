import struct
import os

def generate_bmp_file(file_path):
    # BMP Header
    file_size = 54 + 256 * 3  # Header size + color palette size
    pixel_data_offset = 54  # Header size

    # Bitmap file header
    bmp_header = b'BM'
    bmp_header += struct.pack('<I', file_size)  # File size
    bmp_header += b'\x00\x00\x00\x00'  # Reserved
    bmp_header += struct.pack('<I', pixel_data_offset)  # Pixel data offset

    # DIB Header (BITMAPINFOHEADER)
    dib_header = struct.pack('<I', 40)  # DIB Header size
    dib_header += struct.pack('<I', 256)  # Image width
    dib_header += struct.pack('<I', 256)  # Image height
    dib_header += b'\x01\x00'  # Color planes
    dib_header += b'\x18\x00'  # Bits per pixel (24-bit color)
    dib_header += b'\x00\x00\x00\x00'  # Compression method
    dib_header += struct.pack('<I', 256 * 256 * 3)  # Image data size
    dib_header += b'\x13\x0B\x00\x00'  # Horizontal resolution
    dib_header += b'\x13\x0B\x00\x00'  # Vertical resolution
    dib_header += b'\x00\x00\x00\x00'  # Colors in color palette
    dib_header += b'\x00\x00\x00\x00'  # Important colors

    # Color palette
    color_palette = b''
    for i in range(256):
        color_palette += bytes([i, i, i])

    # Image data
    image_data = b''
    for _ in range(256):
        for _ in range(256):
            image_data += b'\xFF\x00\x00'  # Red pixels

    # Write data to file
    with open(file_path, 'wb') as f:
        f.write(bmp_header)
        f.write(dib_header)
        f.write(color_palette)
        f.write(image_data)

# Create directory if it does not exist
os.makedirs('./tmp/', exist_ok=True)

# Generate BMP file
generate_bmp_file('./tmp/generated_image.bmp')