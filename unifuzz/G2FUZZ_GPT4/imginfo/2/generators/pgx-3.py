from PIL import Image
import numpy as np
import os

# Ensure the ./tmp/ directory exists
output_dir = "./tmp/"
os.makedirs(output_dir, exist_ok=True)

# Image dimensions and bit depth
width, height = 256, 256
bit_depth = 16

# Creating a gradient image
# For 16-bit depth, the maximum value is 65535
gradient = np.zeros((height, width), dtype=np.uint16)
for y in range(height):
    for x in range(width):
        gradient[y, x] = int((x + y) / (width + height) * 65535)

# Convert the numpy array to an Image object and specify mode 'I;16' to denote 16-bit grayscale
image = Image.fromarray(gradient, mode='I;16')

# Save the image in a supported format (e.g., PNG)
image.save(f"{output_dir}gradient.png")

print("PNG file with high bit depth has been generated.")