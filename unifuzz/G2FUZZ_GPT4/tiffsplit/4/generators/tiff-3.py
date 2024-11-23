import numpy as np
import os
from PIL import Image

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Generate an image with high color depth (16 bits per channel)
# Creating a 256x256 image with random colors

# Initialize the image array with zeros
# Each pixel has 3 values (R, G, B), and we want them to be 16-bit, so we use uint16
image_data = np.zeros((256, 256, 3), dtype=np.uint16)

# Populate the array with random values
# np.random.randint generates values within the specified range. For 16-bit, it's 0 to 65535.
image_data[:, :, 0] = np.random.randint(0, 65536, (256, 256), dtype=np.uint16)  # Red channel
image_data[:, :, 1] = np.random.randint(0, 65536, (256, 256), dtype=np.uint16)  # Green channel
image_data[:, :, 2] = np.random.randint(0, 65536, (256, 256), dtype=np.uint16)  # Blue channel

# Create a PIL image from the array
image = Image.fromarray(image_data, mode='I;16')

# Save the image as a TIFF file with high color depth
image.save('./tmp/high_color_depth.tiff')