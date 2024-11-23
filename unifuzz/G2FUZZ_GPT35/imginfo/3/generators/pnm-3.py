import os

def create_pnm_file(filename, width, height, max_val, image_data):
    with open(filename, 'w') as f:
        f.write(f'P3\n{width} {height}\n{max_val}\n')
        for row in image_data:
            for pixel in row:
                f.write(f'{pixel[0]} {pixel[1]} {pixel[2]}\n')

def generate_pnm_file(filename, width, height):
    max_val = 255
    image_data = [[[255, 0, 0] for _ in range(width)] for _ in range(height)]  # Generating a red image
    create_pnm_file(filename, width, height, max_val, image_data)

if not os.path.exists('./tmp'):
    os.makedirs('./tmp')

filename = './tmp/test_image.pnm'
width = 100
height = 100
generate_pnm_file(filename, width, height)