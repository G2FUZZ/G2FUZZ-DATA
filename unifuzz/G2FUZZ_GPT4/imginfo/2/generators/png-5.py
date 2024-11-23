import numpy as np
import matplotlib.pyplot as plt
import os

# Create the tmp directory if it doesn't exist
output_dir = './tmp/'
os.makedirs(output_dir, exist_ok=True)

# Generate an image with a gradient
width, height = 256, 256
gradient = np.tile(np.arange(width, dtype=np.float32) / width, (height, 1))

# Apply gamma correction
# Gamma values < 1 will lighten the image, values > 1 will darken it
gamma_values = [0.5, 1.0, 1.5, 2.0]

for gamma in gamma_values:
    gamma_corrected = np.power(gradient, gamma)
    
    # Plot the gamma corrected image
    plt.figure(figsize=(6, 6))
    plt.imshow(gamma_corrected, cmap='gray', vmin=0, vmax=1)
    plt.axis('off')
    
    # Save the figure
    plt.savefig(f'{output_dir}gamma_{gamma}.png', bbox_inches='tight', pad_inches=0)
    plt.close()