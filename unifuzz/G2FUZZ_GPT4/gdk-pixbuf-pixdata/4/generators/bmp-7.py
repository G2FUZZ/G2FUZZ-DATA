import os

def create_bmp(filename, width, height, color):
    # BMP Header (14 bytes)
    # - Type (2 bytes): BM
    # - Size (4 bytes): Size of the BMP file
    # - Reserved1 (2 bytes): Application specific
    # - Reserved2 (2 bytes): Application specific
    # - Offset (4 bytes): Starting address of the byte where the bitmap data can be found
    bmp_header = b'BM'

    # DIB Header (BITMAPINFOHEADER - 40 bytes)
    # - Size (4 bytes): Size of this header
    # - Width (4 bytes): Bitmap width in pixels
    # - Height (4 bytes): Bitmap height in pixels
    # - Planes (2 bytes): Number of color planes
    # - BitCount (2 bytes): Number of bits per pixel
    # - Compression (4 bytes): Compression type (0 = none)
    # - SizeImage (4 bytes): Image size (can be 0 for BI_RGB)
    # - XpixelsPerMeter (4 bytes): Horizontal resolution
    # - YpixelsPerMeter (4 bytes): Vertical resolution
    # - ColorsUsed (4 bytes): Number of colors in the palette
    # - ColorsImportant (4 bytes): 0 means all colors are important
    dib_header_size = 40
    planes = 1
    bit_count = 24
    compression = 0
    size_image = width * height * 3
    x_pixels_per_meter = 2835
    y_pixels_per_meter = 2835
    colors_used = 0
    colors_important = 0

    # Calculate total size of the BMP file
    offset = 14 + 40  # File header + DIB header size
    file_size = offset + size_image

    # Create file header and DIB header
    file_header = bmp_header + file_size.to_bytes(4, byteorder='little') + (0).to_bytes(4, byteorder='little') + offset.to_bytes(4, byteorder='little')
    dib_header = (dib_header_size.to_bytes(4, byteorder='little') +
                  width.to_bytes(4, byteorder='little') + 
                  height.to_bytes(4, byteorder='little') + 
                  planes.to_bytes(2, byteorder='little') + 
                  bit_count.to_bytes(2, byteorder='little') + 
                  compression.to_bytes(4, byteorder='little') + 
                  size_image.to_bytes(4, byteorder='little') + 
                  x_pixels_per_meter.to_bytes(4, byteorder='little') + 
                  y_pixels_per_meter.to_bytes(4, byteorder='little') + 
                  colors_used.to_bytes(4, byteorder='little') + 
                  colors_important.to_bytes(4, byteorder='little'))

    # Pixel data (simple color fill for demonstration)
    pixel_data = bytearray([color[2], color[1], color[0]] * width * height)

    # Write to file
    with open(filename, 'wb') as f:
        f.write(file_header + dib_header + pixel_data)

# Ensure the tmp directory exists
os.makedirs('./tmp/', exist_ok=True)

# Create a simple BMP file with a specific color
create_bmp('./tmp/simple_image.bmp', 100, 100, (255, 0, 0))  # Red color fill