import numpy as np
from PIL import Image

# Function to apply gamma correction
def adjust_gamma(image, gamma=1.0):
    invGamma = 1.0 / gamma
    table = [((i / 255.0) ** invGamma) * 255 for i in range(256)]
    # Replicate the table for each channel (R, G, B)
    table = np.array(table * 3, np.uint8)  # This ensures the table is the correct size for RGB images
    return Image.fromarray(np.array(image).astype(np.uint8)).point(table)

# Create a gradient image
width, height = 256, 256
gradient = np.tile(np.linspace(0, 255, width, dtype=np.uint8), (height, 1))

# Convert the gradient into an RGB image
gradient_image = Image.fromarray(np.stack([gradient]*3, axis=-1))

# Apply gamma correction
gamma_corrected = adjust_gamma(gradient_image, gamma=2.2)

# Ensure the ./tmp/ directory exists
import os
if not os.path.exists('./tmp/'):
    os.makedirs('./tmp/')

# Save the gamma corrected image
gamma_corrected.save('./tmp/gamma_corrected.png')