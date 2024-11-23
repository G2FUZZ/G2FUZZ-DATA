import os

def generate_pnm_file(filename, width, height, max_pixel_value, pixel_data):
    with open(filename, 'w') as f:
        f.write(f'P3\n{width} {height}\n{max_pixel_value}\n')
        for row in pixel_data:
            for pixel in row:
                f.write(f'{pixel[0]} {pixel[1]} {pixel[2]} ')
            f.write('\n')

def create_tmp_dir():
    if not os.path.exists('./tmp'):
        os.makedirs('./tmp')

width = 3
height = 3
max_pixel_value = 255
pixel_data = [
    [(255, 0, 0), (0, 255, 0), (0, 0, 255)],
    [(255, 255, 0), (255, 0, 255), (0, 255, 255)],
    [(128, 128, 128), (0, 0, 0), (255, 255, 255)]
]

create_tmp_dir()
generate_pnm_file('./tmp/test.pnm', width, height, max_pixel_value, pixel_data)