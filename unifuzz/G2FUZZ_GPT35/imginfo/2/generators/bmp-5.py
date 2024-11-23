import struct

def generate_bmp_with_metadata(width, height, resolution=(300, 300), color_profile='sRGB', creation_date='2022-01-01'):
    # BMP header
    file_size = 14 + 40 + width * height * 3  # 14 for file header, 40 for info header
    pixel_data_offset = 14 + 40
    file_header = b'BM' + struct.pack('<I', file_size) + b'\x00\x00\x00\x00' + struct.pack('<I', pixel_data_offset)
    
    # BMP info header
    info_header_size = 40
    planes = 1
    bits_per_pixel = 24
    compression = 0
    image_size = 0
    x_pixels_per_meter = int(resolution[0] * 39.3701)  # Convert from DPI to DPM
    y_pixels_per_meter = int(resolution[1] * 39.3701)
    colors_used = 0
    important_colors = 0
    info_header = struct.pack('<IiiHHIIIIII', info_header_size, width, height, planes, bits_per_pixel, compression, 
                              image_size, x_pixels_per_meter, y_pixels_per_meter, colors_used, important_colors)
    
    # Create the pixel data (for simplicity, fill with white pixels)
    pixel_data = b'\xFF\xFF\xFF' * width * height
    
    # Write to file
    with open(f'./tmp/metadata_image.bmp', 'wb') as f:
        f.write(file_header + info_header + pixel_data)

# Generate BMP file with metadata
generate_bmp_with_metadata(640, 480)