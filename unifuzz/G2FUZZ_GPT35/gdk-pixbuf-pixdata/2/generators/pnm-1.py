import os

def create_pnm_file(width, height, max_val, pixels, output_file):
    with open(output_file, 'w') as f:
        f.write(f'P3\n{width} {height}\n{max_val}\n')
        for pixel in pixels:
            f.write(' '.join(map(str, pixel)) + '\n')

def generate_pnm_files():
    if not os.path.exists('./tmp'):
        os.makedirs('./tmp')

    # Generate PNM file 1
    width = 3
    height = 2
    max_val = 255
    pixels = [
        [255, 0, 0], [0, 255, 0], [0, 0, 255],
        [255, 255, 0], [255, 0, 255], [0, 255, 255]
    ]
    create_pnm_file(width, height, max_val, pixels, './tmp/pnm_file1.pnm')

    # Generate PNM file 2
    width = 2
    height = 2
    max_val = 255
    pixels = [
        [255, 255, 255], [0, 0, 0],
        [128, 0, 0], [0, 128, 0]
    ]
    create_pnm_file(width, height, max_val, pixels, './tmp/pnm_file2.pnm')

if __name__ == '__main__':
    generate_pnm_files()