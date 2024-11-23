import os
from struct import pack

def create_bmp_file(file_path, width, height, color=(0, 0, 255)):
    """
    Creates a simple BMP file with a single color.
    
    Args:
    - file_path: Path to save the BMP file.
    - width: Width of the image.
    - height: Height of the image.
    - color: A tuple representing the RGB color of the image.
    """
    # Ensure the tmp directory exists
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    
    # BMP Header components
    file_type = b'BM'
    file_size = 14 + 40 + (width * height * 3)  # File header + Info header + Pixel data
    reserved_1 = 0
    reserved_2 = 0
    offset = 14 + 40  # File header + Info header
    
    # BITMAPINFOHEADER components
    header_size = 40
    planes = 1
    bit_count = 24  # 24 bits per pixel
    compression = 0
    size_image = width * height * 3
    x_pixels_per_meter = 0
    y_pixels_per_meter = 0
    colors_used = 0
    colors_important = 0
    
    # Create the file header
    file_header = pack('<2sIHHI', file_type, file_size, reserved_1, reserved_2, offset)
    
    # Create the info header
    info_header = pack('<IIIHHIIIIII', header_size, width, height, planes, bit_count,
                       compression, size_image, x_pixels_per_meter, y_pixels_per_meter,
                       colors_used, colors_important)
                       
    # Create pixel data
    pixel_data = bytearray([color[2], color[1], color[0]] * width * height)
    
    # Write to file
    with open(file_path, 'wb') as f:
        f.write(file_header)
        f.write(info_header)
        f.write(pixel_data)

# Example usage
create_bmp_file('./tmp/example.bmp', 100, 100, (255, 0, 0))  # Creates a 100x100 red BMP image