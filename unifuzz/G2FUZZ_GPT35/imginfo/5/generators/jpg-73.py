import numpy as np
from PIL import Image

# Create a gradient color image
height, width = 200, 300
gradient_image = np.zeros((height, width, 3), dtype=np.uint8)

for i in range(height):
    for j in range(width):
        gradient_image[i, j] = [int(255 * i / height), int(255 * j / width), int(255 * (i + j) / (height + width))]

gradient_image = Image.fromarray(gradient_image)

# Save the gradient image with .jpg extension
gradient_image.save("./tmp/gradient_image.jpg")