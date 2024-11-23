import os

def create_pnm_file(file_path, format_type, data):
    with open(file_path, 'w') as file:
        file.write(f'{format_type}\n')  # Writing the format type
        for row in data:
            file.write(' '.join(row) + '\n')  # Writing each row in the data

def generate_pbm_file(file_name):
    data = [['0', '1'],
            ['1', '0']]
    create_pnm_file(file_name, 'P1', data)

def generate_pgm_file(file_name):
    data = [['255', '128'],
            ['64', '192']]
    create_pnm_file(file_name, 'P2', data)

def generate_ppm_file(file_name):
    data = [['255', '128', '64'],
            ['192', '0', '255']]
    create_pnm_file(file_name, 'P3', data)

if not os.path.exists('./tmp'):
    os.makedirs('./tmp')

generate_pbm_file('./tmp/test_pbm.pbm')
generate_pgm_file('./tmp/test_pgm.pgm')
generate_ppm_file('./tmp/test_ppm.ppm')