import os
import numpy as np

# Create the tmp directory if it doesn't exist
if not os.path.exists('./tmp'):
    os.makedirs('./tmp')

# Function to save a grayscale image (PGM)
def save_pgm(image, filename):
    maxval = 255
    height, width = image.shape
    with open(filename, 'w') as f:
        f.write("P2\n")
        f.write(f"{width} {height}\n")
        f.write(f"{maxval}\n")
        for row in image:
            for val in row:
                f.write(f"{val} ")
            f.write("\n")

# Function to save a color image (PPM)
def save_ppm(image, filename):
    maxval = 255
    height, width, _ = image.shape
    with open(filename, 'w') as f:
        f.write("P3\n")
        f.write(f"{width} {height}\n")
        f.write(f"{maxval}\n")
        for row in image:
            for colors in row:
                f.write(' '.join(map(str, colors)) + " ")
            f.write("\n")

# Generate a grayscale image
grayscale_image = np.random.randint(0, 256, (100, 100), dtype=np.uint8)
save_pgm(grayscale_image, './tmp/grayscale_image.pgm')

# Generate a color image
color_image = np.random.randint(0, 256, (100, 100, 3), dtype=np.uint8)
save_ppm(color_image, './tmp/color_image.ppm')