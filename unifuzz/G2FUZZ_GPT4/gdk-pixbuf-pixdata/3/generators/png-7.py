from PIL import Image, PngImagePlugin
import numpy as np
import os

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Create a simple 100x100 red image
image_data = np.zeros((100, 100, 3), dtype=np.uint8)
image_data[:, :] = [255, 0, 0]  # RGB Red
img = Image.fromarray(image_data, 'RGB')

# Save the image without explicitly embedding an external sRGB profile
img.save('./tmp/colored_img.png')