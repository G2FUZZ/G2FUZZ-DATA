import os

def generate_pnm_file(file_path, width, height, max_val, pixels):
    with open(file_path, 'w') as f:
        f.write(f'P2\n{width} {height}\n{max_val}\n')
        for row in pixels:
            f.write(' '.join(map(str, row)) + '\n')

def main():
    if not os.path.exists('./tmp'):
        os.makedirs('./tmp')
    
    width, height = 5, 5
    max_val = 255
    pixels = [[0, 255, 0, 255, 0],
              [255, 0, 255, 0, 255],
              [0, 255, 0, 255, 0],
              [255, 0, 255, 0, 255],
              [0, 255, 0, 255, 0]]
    
    file_path = './tmp/sample.pgm'
    generate_pnm_file(file_path, width, height, max_val, pixels)
    print(f'PNM file generated at {file_path}')

if __name__ == '__main__':
    main()