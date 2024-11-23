import numpy as np

def save_pnm_file(filename, image, color_depth=255):
    with open(filename, 'w') as f:
        if image.ndim == 2:  # PGM file
            f.write("P2\n")
            f.write(f"{image.shape[1]} {image.shape[0]}\n")
            f.write(f"{color_depth}\n")
            for row in image:
                f.write(" ".join(str(int(pixel)) for pixel in row) + "\n")
        elif image.ndim == 3:  # PPM file
            f.write("P3\n")
            f.write(f"{image.shape[1]} {image.shape[0]}\n")
            f.write(f"{color_depth}\n")
            for row in image:
                for pixel in row:
                    f.write(" ".join(str(int(channel)) for channel in pixel) + " ")

image_complex = np.array([[[255, 0, 0], [0, 255, 0], [0, 0, 255]],
                          [[255, 255, 0], [255, 0, 255], [0, 255, 255]],
                          [[128, 128, 128], [64, 192, 128], [128, 128, 64]],
                          [[200, 100, 50], [150, 50, 200], [100, 200, 150]]])

save_pnm_file('./tmp/image_complex.pnm', image_complex, color_depth=255)