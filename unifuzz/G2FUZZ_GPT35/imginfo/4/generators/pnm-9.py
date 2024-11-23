import os

def create_pnm_file(file_path, width, height, max_val, pixel_data):
    with open(file_path, 'w') as file:
        file.write(f'P2\n{width} {height}\n{max_val}\n')
        for row in range(height):
            row_data = ' '.join(str(val) for val in pixel_data[row * width:(row + 1) * width])
            file.write(row_data + '\n')

def generate_simple_pnm_file(file_path):
    width = 5
    height = 5
    max_val = 255
    pixel_data = [x % 256 for x in range(width * height)]
    create_pnm_file(file_path, width, height, max_val, pixel_data)

if not os.path.exists('./tmp/'):
    os.makedirs('./tmp/')

file_path = './tmp/simple_structure.pnm'
generate_simple_pnm_file(file_path)
print(f'PNM file with simple structure generated: {file_path}')