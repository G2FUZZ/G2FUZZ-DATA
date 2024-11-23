import os

def generate_pnm_file(file_name, width, height, max_value):
    file_path = os.path.join('./tmp/', file_name)
    with open(file_path, 'w') as file:
        file.write(f'P2\n{width} {height}\n{max_value}\n')
        for i in range(1, width * height + 1):
            file.write(f'{i % (max_value + 1)} ')
            if i % width == 0:
                file.write('\n')

if not os.path.exists('./tmp/'):
    os.makedirs('./tmp/')

file_name = 'sample.pnm'
width = 10
height = 10
max_value = 255

generate_pnm_file(file_name, width, height, max_value)