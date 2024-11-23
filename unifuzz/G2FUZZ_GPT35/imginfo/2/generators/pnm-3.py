import numpy as np

def create_pbm_file():
    # PBM file for black and white images
    width, height = 10, 10
    data = np.random.randint(0, 2, (height, width), dtype=np.uint8)
    with open('./tmp/file.pbm', 'w') as file:
        file.write("P1\n{} {}\n".format(width, height))
        for row in data:
            file.write(" ".join(str(pixel) for pixel in row) + '\n')

def create_pgm_file():
    # PGM file for grayscale images
    width, height = 10, 10
    data = np.random.randint(0, 256, (height, width), dtype=np.uint8)
    with open('./tmp/file.pgm', 'w') as file:
        file.write("P2\n{} {}\n255\n".format(width, height))
        for row in data:
            file.write(" ".join(str(pixel) for pixel in row) + '\n')

def create_ppm_file():
    # PPM file for color images
    width, height = 10, 10
    data_r = np.random.randint(0, 256, (height, width), dtype=np.uint8)
    data_g = np.random.randint(0, 256, (height, width), dtype=np.uint8)
    data_b = np.random.randint(0, 256, (height, width), dtype=np.uint8)
    with open('./tmp/file.ppm', 'w') as file:
        file.write("P3\n{} {}\n255\n".format(width, height))
        for r, g, b in zip(data_r, data_g, data_b):
            file.write(" ".join(str(pixel) for pixel in r) + ' ')
            file.write(" ".join(str(pixel) for pixel in g) + ' ')
            file.write(" ".join(str(pixel) for pixel in b) + '\n')

create_pbm_file()
create_pgm_file()
create_ppm_file()