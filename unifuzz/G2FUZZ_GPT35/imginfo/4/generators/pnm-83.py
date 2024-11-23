import numpy as np

def create_pnm_file(color_depth, filename):
    if color_depth == 1:
        image_data = np.random.randint(0, 2, size=(100, 100), dtype=np.uint8)
        file_type = b'P4'
    elif color_depth == 8:
        image_data = np.random.randint(0, 256, size=(100, 100), dtype=np.uint8)
        file_type = b'P5'
    elif color_depth == 24:
        image_data = np.random.randint(0, 256, size=(100, 100, 3), dtype=np.uint8)
        file_type = b'P6'
    
    with open(filename, 'wb') as f:
        f.write(file_type + b'\n100 100\n')
        if color_depth == 1:
            f.write(image_data.tobytes())
        elif color_depth == 8 or color_depth == 24:
            f.write(b'255\n')
            f.write(image_data.tobytes())

# Create PNM files with different color depths
create_pnm_file(1, './tmp/black_white_image.pbm')
create_pnm_file(8, './tmp/grayscale_image.pgm')
create_pnm_file(24, './tmp/color_image.ppm')