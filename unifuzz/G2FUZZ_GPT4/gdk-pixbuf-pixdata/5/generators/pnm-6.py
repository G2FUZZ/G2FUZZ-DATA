import os
import numpy as np

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Generating a grayscale image (PGM)
def generate_pgm_file(filepath, width, height, max_val, data):
    header = f"P5\n{width} {height}\n{max_val}\n"
    with open(filepath, 'wb') as f:
        f.write(bytearray(header, 'ascii'))
        f.write(data.tobytes())

# Generating a color image (PPM)
def generate_ppm_file(filepath, width, height, max_val, data):
    header = f"P6\n{width} {height}\n{max_val}\n"
    with open(filepath, 'wb') as f:
        f.write(bytearray(header, 'ascii'))
        f.write(data.tobytes())

# Example parameters for the images
width, height = 100, 100
max_val = 255

# Create a simple gradient for the grayscale image
grayscale_data = np.tile(np.linspace(0, max_val, width, dtype=np.uint8), (height, 1))

# Create a simple color gradient for the color image
color_data = np.zeros((height, width, 3), dtype=np.uint8)
color_data[:, :, 0] = np.tile(np.linspace(0, max_val, width, dtype=np.uint8), (height, 1))  # Red channel
color_data[:, :, 1] = np.tile(np.linspace(max_val, 0, width, dtype=np.uint8), (height, 1))  # Green channel
color_data[:, :, 2] = np.tile(np.linspace(0, max_val//2, width, dtype=np.uint8), (height, 1))  # Blue channel

# Generate the files
generate_pgm_file('./tmp/sample_grayscale.pgm', width, height, max_val, grayscale_data)
generate_ppm_file('./tmp/sample_color.ppm', width, height, max_val, color_data)

print("Grayscale and color PNM files have been generated in ./tmp/")