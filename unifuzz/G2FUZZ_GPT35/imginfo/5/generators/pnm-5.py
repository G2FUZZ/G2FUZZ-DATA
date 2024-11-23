import os

def generate_pnm_file(file_name, width, height, max_pixel_value):
    header = f'P3\n{width} {height}\n{max_pixel_value}\n'
    pixels = ''
    for i in range(height):
        for j in range(width):
            pixels += f'{i % max_pixel_value} {j % max_pixel_value} {(i+j) % max_pixel_value} '
    with open(file_name, 'w') as file:
        file.write(header + pixels.strip())

if not os.path.exists('./tmp'):
    os.makedirs('./tmp')

file_name = './tmp/sample.pnm'
width = 10
height = 10
max_pixel_value = 255
generate_pnm_file(file_name, width, height, max_pixel_value)