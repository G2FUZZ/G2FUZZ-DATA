import os
from struct import pack

def create_bmp_file(file_path, width, height, color=(0, 0, 255)):
    """
    Create a BMP file with a specified width, height, and color.

    Args:
        file_path (str): Path to save the BMP file.
        width (int): The width of the image.
        height (int): The height of the image.
        color (tuple): A tuple representing the RGB color (default is blue).
    """
    # BMP Header
    file_type = b'BM'  # BM indicates a bitmap
    reserved_1 = 0
    reserved_2 = 0
    offset = 54  # where the pixel array can be found
    file_size = offset + width * height * 3  # header size + pixel array size

    # DIB Header (BITMAPINFOHEADER)
    dib_header_size = 40
    planes = 1
    bits_per_pixel = 24
    compression = 0
    image_size = width * height * 3
    ppm_x = 0
    ppm_y = 0
    num_colors = 0
    important_colors = 0

    # Create the headers
    file_header = pack('<2sIHHI', file_type, file_size, reserved_1, reserved_2, offset)
    info_header = pack('<IIIHHIIIIII', dib_header_size, width, height, planes, bits_per_pixel,
                       compression, image_size, ppm_x, ppm_y, num_colors, important_colors)

    # Ensure the directory exists
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    
    with open(file_path, 'wb') as bmp_file:
        bmp_file.write(file_header)
        bmp_file.write(info_header)

        # Write the pixel array
        for y in range(height):
            for x in range(width):
                bmp_file.write(pack('<BBB', *color))
                
# Example usage
create_bmp_file('./tmp/blue_square.bmp', 100, 100)