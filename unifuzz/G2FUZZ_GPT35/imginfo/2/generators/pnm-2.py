import os

def create_pbm_file():
    # PBM (monochrome) file
    width, height = 10, 10
    pixel_data = ' '.join(['1' if (i+j) % 2 == 0 else '0' for i in range(width) for j in range(height)])
    with open('./tmp/monochrome.pbm', 'w') as file:
        file.write(f'P1\n{width} {height}\n{pixel_data}\n')

def create_pgm_file():
    # PGM (grayscale) file
    width, height = 10, 10
    max_gray_value = 255
    pixel_data = ' '.join([str((i+j) % max_gray_value) for i in range(width) for j in range(height)])
    with open('./tmp/grayscale.pgm', 'w') as file:
        file.write(f'P2\n{width} {height}\n{max_gray_value}\n{pixel_data}\n')

def create_ppm_file():
    # PPM (color) file
    width, height = 10, 10
    max_color_value = 255
    pixel_data = ' '.join([f'{(i+j) % max_color_value} {(i+j) % max_color_value} {(i+j) % max_color_value}' for i in range(width) for j in range(height)])
    with open('./tmp/color.ppm', 'w') as file:
        file.write(f'P3\n{width} {height}\n{max_color_value}\n{pixel_data}\n')

if not os.path.exists('./tmp'):
    os.makedirs('./tmp')

create_pbm_file()
create_pgm_file()
create_ppm_file()