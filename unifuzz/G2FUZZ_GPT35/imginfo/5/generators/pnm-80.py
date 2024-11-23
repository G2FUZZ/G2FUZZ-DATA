import os

def create_pnm_file(file_path, format_type, width, height, max_val, data):
    with open(file_path, 'w') as file:
        file.write(f'{format_type}\n')
        file.write(f'{width} {height}\n')
        file.write(f'{max_val}\n')
        for row in data:
            file.write(' '.join(row) + '\n')

def generate_custom_pnm_file(file_name):
    width = 4
    height = 4
    max_val = 255
    data = [['255', '128', '64', '0'],
            ['192', '0', '255', '128'],
            ['64', '128', '192', '64'],
            ['0', '192', '128', '255']]
    create_pnm_file(file_name, 'P3', width, height, max_val, data)

if not os.path.exists('./tmp'):
    os.makedirs('./tmp')

generate_custom_pnm_file('./tmp/test_custom.pnm')