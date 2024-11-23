import numpy as np
import os

def create_bmp_file(color_depth, file_path):
    if color_depth not in [1, 4, 8, 24]:
        print("Unsupported color depth")
        return

    if color_depth == 1:
        img = np.random.randint(0, 2, size=(100, 100))  # 1-bit monochrome
    elif color_depth == 4:
        img = np.random.randint(0, 16, size=(100, 100))  # 4-bit color
    elif color_depth == 8:
        img = np.random.randint(0, 256, size=(100, 100))  # 8-bit color
    else:
        img = np.random.randint(0, 256, size=(100, 100, 3))  # 24-bit true color

    img = np.uint8(img)

    if not os.path.exists(os.path.dirname(file_path)):
        os.makedirs(os.path.dirname(file_path))

    if color_depth == 1:
        img.tofile(file_path)
    else:
        if color_depth == 24:
            img.tofile(file_path)
        else:
            with open(file_path, 'wb') as f:
                f.write(bytearray([color_depth] * 54))
                img.tofile(f)

# Generate and save BMP files with different color depths
create_bmp_file(1, './tmp/1_bit.bmp')
create_bmp_file(4, './tmp/4_bit.bmp')
create_bmp_file(8, './tmp/8_bit.bmp')
create_bmp_file(24, './tmp/24_bit.bmp')