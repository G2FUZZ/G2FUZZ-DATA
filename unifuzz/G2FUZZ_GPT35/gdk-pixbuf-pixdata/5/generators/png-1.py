import numpy as np
from PIL import Image

# Creating a simple image with numpy
image_data = np.zeros((100, 100, 3), dtype=np.uint8)
image_data[50:80, 20:70] = [255, 0, 0]  # Red rectangle in the image

# Saving the image as a PNG file
img = Image.fromarray(image_data)
img.save('./tmp/lossless_compression.png')