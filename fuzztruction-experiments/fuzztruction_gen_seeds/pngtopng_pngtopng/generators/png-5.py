import numpy as np
import matplotlib.pyplot as plt
import os

# Ensure the ./tmp/ directory exists
output_dir = './tmp/'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Create an image with varying brightness
width, height = 256, 256
image = np.zeros((height, width), dtype=np.uint8)

# Create a gradient from left (black) to right (white)
for x in range(width):
    image[:, x] = x

# Apply gamma correction
gamma = 0.5  # Gamma less than 1 - light areas will be emphasized
image_gamma_corrected = np.array(255 * (image / 255) ** gamma, dtype='uint8')

# Save the original and gamma-corrected images
plt.imsave(f'{output_dir}original.png', image, cmap='gray')
plt.imsave(f'{output_dir}gamma_corrected.png', image_gamma_corrected, cmap='gray')