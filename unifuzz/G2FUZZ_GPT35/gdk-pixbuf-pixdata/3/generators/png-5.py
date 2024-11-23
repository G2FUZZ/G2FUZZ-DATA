import numpy as np
from PIL import Image

# Create a simple image with a gradient for demonstration
width, height = 256, 256
image = np.zeros((height, width, 3), dtype=np.uint8)

for i in range(width):
    image[:, i] = [i, 255-i, 128]  # Gradient from left to right

# Create an interlaced PNG image
interlaced_image = Image.fromarray(image)
interlaced_image.save('./tmp/interlaced_image.png', interlace=True)

print("Interlaced PNG file saved successfully.")