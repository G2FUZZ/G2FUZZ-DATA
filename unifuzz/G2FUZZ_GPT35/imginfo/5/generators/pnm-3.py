import numpy as np

def save_pbm_file(filename, image):
    with open(filename, 'w') as f:
        f.write("P1\n")
        f.write(f"{image.shape[1]} {image.shape[0]}\n")
        for row in image:
            f.write(" ".join(str(int(pixel)) for pixel in row) + "\n")

def save_pgm_file(filename, image):
    with open(filename, 'w') as f:
        f.write("P2\n")
        f.write(f"{image.shape[1]} {image.shape[0]}\n")
        f.write("255\n")
        for row in image:
            f.write(" ".join(str(int(pixel)) for pixel in row) + "\n")

def save_ppm_file(filename, image):
    with open(filename, 'w') as f:
        f.write("P3\n")
        f.write(f"{image.shape[1]} {image.shape[0]}\n")
        f.write("255\n")
        for row in image:
            for pixel in row:
                f.write(" ".join(str(int(channel)) for channel in pixel) + " ")

image_pbm = np.array([[0, 1, 0],
                      [1, 0, 1],
                      [0, 1, 0]])

image_pgm = np.array([[100, 150, 200],
                      [50, 75, 100],
                      [25, 125, 175]])

image_ppm = np.array([[[255, 0, 0], [0, 255, 0], [0, 0, 255]],
                      [[255, 255, 0], [255, 0, 255], [0, 255, 255]],
                      [[128, 128, 128], [64, 192, 128], [128, 128, 64]]])

save_pbm_file('./tmp/image_pbm.pbm', image_pbm)
save_pgm_file('./tmp/image_pgm.pgm', image_pgm)
save_ppm_file('./tmp/image_ppm.ppm', image_ppm)