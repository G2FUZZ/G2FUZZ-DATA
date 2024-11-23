import os
import numpy as np

# Create the ./tmp/ directory if it doesn't already exist
os.makedirs("./tmp/", exist_ok=True)

# Function to save a PBM (Portable BitMap) file
def save_pbm(filename, data):
    height, width = data.shape
    header = f"P1\n{width} {height}\n"
    body = "\n".join(" ".join(str(pixel) for pixel in row) for row in data)
    with open(filename, "w") as file:
        file.write(header + body)

# Function to save a PGM (Portable GrayMap) file
def save_pgm(filename, data):
    height, width = data.shape
    max_val = 255  # Assuming 8-bit grayscale
    header = f"P2\n{width} {height}\n{max_val}\n"
    body = "\n".join(" ".join(str(pixel) for pixel in row) for row in data)
    with open(filename, "w") as file:
        file.write(header + body)

# Function to save a PPM (Portable PixMap) file
def save_ppm(filename, data):
    height, width, _ = data.shape
    max_val = 255  # Assuming 8-bit color depth
    header = f"P3\n{width} {height}\n{max_val}\n"
    body = "\n".join(" ".join(" ".join(str(value) for value in pixel) for pixel in row) for row in data)
    with open(filename, "w") as file:
        file.write(header + body)

# Generate a binary image for PBM
pbm_data = np.random.randint(0, 2, (100, 100), dtype=np.uint8)
save_pbm("./tmp/sample.pbm", pbm_data)

# Generate a grayscale image for PGM
pgm_data = np.random.randint(0, 256, (100, 100), dtype=np.uint8)
save_pgm("./tmp/sample.pgm", pgm_data)

# Generate a color image for PPM
ppm_data = np.random.randint(0, 256, (100, 100, 3), dtype=np.uint8)
save_ppm("./tmp/sample.ppm", ppm_data)