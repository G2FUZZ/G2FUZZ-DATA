import os
import random

def generate_complex_pnm_file(metadata, width, height):
    file_name = os.path.join('./tmp/', 'generated_complex_image.pnm')
    with open(file_name, 'w') as file:
        file.write(f'P3\n#{metadata}\n{width} {height}\n255\n')
        for _ in range(height):
            for _ in range(width):
                red = random.randint(0, 255)
                green = random.randint(0, 255)
                blue = random.randint(0, 255)
                file.write(f'{red} {green} {blue} ')
            file.write('\n')

metadata = 'Complex Metadata: This pnm file contains randomly generated RGB colors.'
width = 8
height = 6
generate_complex_pnm_file(metadata, width, height)