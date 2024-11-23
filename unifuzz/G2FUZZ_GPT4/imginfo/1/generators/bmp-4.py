import os
import random

def create_bmp(filename, width, height):
    # BMP Header
    file_type = b'BM'
    reserved1 = reserved2 = 0
    offset = 54  # BMP header size
    file_size = offset + width * height * 3  # 3 bytes per pixel

    # DIB Header
    dib_header_size = 40
    planes = 1
    bits_per_pixel = 24
    compression = 0
    image_size = width * height * 3
    x_ppm = y_ppm = 0  # Pixels per meter
    colors_used = colors_important = 0

    # Ensure ./tmp/ directory exists
    os.makedirs('./tmp/', exist_ok=True)
    filepath = os.path.join('./tmp/', filename)

    with open(filepath, 'wb') as bmp_file:
        # Write file header
        bmp_file.write(file_type)
        bmp_file.write(file_size.to_bytes(4, byteorder='little'))
        bmp_file.write(reserved1.to_bytes(2, byteorder='little'))
        bmp_file.write(reserved2.to_bytes(2, byteorder='little'))
        bmp_file.write(offset.to_bytes(4, byteorder='little'))

        # Write DIB header
        bmp_file.write(dib_header_size.to_bytes(4, byteorder='little'))
        bmp_file.write(width.to_bytes(4, byteorder='little'))
        bmp_file.write(height.to_bytes(4, byteorder='little'))
        bmp_file.write(planes.to_bytes(2, byteorder='little'))
        bmp_file.write(bits_per_pixel.to_bytes(2, byteorder='little'))
        bmp_file.write(compression.to_bytes(4, byteorder='little'))
        bmp_file.write(image_size.to_bytes(4, byteorder='little'))
        bmp_file.write(x_ppm.to_bytes(4, byteorder='little'))
        bmp_file.write(y_ppm.to_bytes(4, byteorder='little'))
        bmp_file.write(colors_used.to_bytes(4, byteorder='little'))
        bmp_file.write(colors_important.to_bytes(4, byteorder='little'))

        # Write pixel data
        for y in range(height):
            for x in range(width):
                r = random.randint(0, 255)
                g = random.randint(0, 255)
                b = random.randint(0, 255)
                bmp_file.write(b.to_bytes(1, byteorder='little'))
                bmp_file.write(g.to_bytes(1, byteorder='little'))
                bmp_file.write(r.to_bytes(1, byteorder='little'))

# Example usage
create_bmp('example.bmp', 100, 100)