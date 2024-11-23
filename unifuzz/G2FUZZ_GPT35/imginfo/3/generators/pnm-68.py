import os

def create_pnm_file(filename, width, height, max_val, image_data):
    with open(filename, 'w') as f:
        f.write(f'P2\n{width} {height}\n{max_val}\n')
        for row in image_data:
            for pixel in row:
                f.write(f'{pixel} ')

def generate_pnm_file(filename, width, height):
    max_val = 255
    image_data = [[int((x + y) / 2) for x in range(width)] for y in range(height)]  # Generating a grayscale gradient image
    create_pnm_file(filename, width, height, max_val, image_data)

if not os.path.exists('./tmp'):
    os.makedirs('./tmp')

filename = './tmp/gradient_image.pnm'
width = 100
height = 100
generate_pnm_file(filename, width, height)