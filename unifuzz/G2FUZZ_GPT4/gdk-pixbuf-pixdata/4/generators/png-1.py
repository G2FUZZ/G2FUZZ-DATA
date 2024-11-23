import numpy as np
import matplotlib.pyplot as plt
import os

# Ensure the ./tmp/ directory exists
output_dir = "./tmp/"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Generate an image with detailed patterns
image_size = (256, 256)
x, y = np.meshgrid(np.linspace(0, 4*np.pi, image_size[0]), np.linspace(0, 4*np.pi, image_size[1]))
z = np.sin(x) + np.cos(y)

# Plot the image
plt.figure(figsize=(6, 6))
plt.imshow(z, cmap='viridis', interpolation='nearest')
plt.axis('off')  # Do not show axis to highlight the pattern

# Save the image with lossless compression
plt.savefig(f"{output_dir}/lossless_compression_example.png", format='png', bbox_inches='tight', pad_inches=0)

plt.close()