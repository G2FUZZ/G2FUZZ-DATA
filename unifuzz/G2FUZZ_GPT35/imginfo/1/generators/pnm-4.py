import os

def create_pnm_file(file_path, width, height, max_val, pixels):
    with open(file_path, 'w') as f:
        f.write(f'P2\n{width} {height}\n{max_val}\n')
        for row in pixels:
            f.write(' '.join(str(pixel) for pixel in row) + '\n')

def generate_pnm_file(file_name):
    width, height = 5, 5
    max_val = 255
    pixels = [[i + j for i in range(width)] for j in range(height)]
    file_path = f'./tmp/{file_name}.pnm'
    create_pnm_file(file_path, width, height, max_val, pixels)

if not os.path.exists('./tmp'):
    os.makedirs('./tmp')

generate_pnm_file('image1')
generate_pnm_file('image2')