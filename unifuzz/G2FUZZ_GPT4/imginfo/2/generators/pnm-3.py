import numpy as np
import os

# Create the directory for the output files if it doesn't already exist
output_dir = './tmp/'
os.makedirs(output_dir, exist_ok=True)

# Function to save PGM (grayscale) image
def save_pgm(image, filename):
    max_val = 255
    with open(filename, 'w') as f:
        f.write(f"P2\n{image.shape[1]} {image.shape[0]}\n{max_val}\n")
        for row in image:
            for val in row:
                f.write(f"{val} ")
            f.write("\n")

# Function to save PPM (color) image
def save_ppm(image, filename):
    max_val = 255
    with open(filename, 'w') as f:
        f.write(f"P3\n{image.shape[1]} {image.shape[0]}\n{max_val}\n")
        for row in image:
            for pixel in row:
                f.write(f"{' '.join(str(val) for val in pixel)} ")
            f.write("\n")

# Generate and save a grayscale image
width, height = 100, 50
gray_image = np.random.randint(0, 256, (height, width), dtype=np.uint8)
save_pgm(gray_image, os.path.join(output_dir, 'grayscale.pgm'))

# Generate and save a color image
color_image = np.random.randint(0, 256, (height, width, 3), dtype=np.uint8)
save_ppm(color_image, os.path.join(output_dir, 'color.ppm'))