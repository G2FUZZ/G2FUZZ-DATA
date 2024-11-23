import numpy as np
import imageio
import os

# Define the image dimensions (width, height)
width, height = 256, 256

# Create an empty image with 3 color channels (RGB), filled with zeros
# Each pixel's color is represented as [R, G, B]
image = np.zeros((height, width, 3), dtype=np.uint8)

# Fill the image with a gradient
# The left side of the image will be red, fading to blue on the right side
for x in range(width):
    for y in range(height):
        image[y, x] = [x, 0, 255 - x]  # Setting the pixel value

# Ensure the ./tmp/ directory exists
if not os.path.exists('./tmp/'):
    os.makedirs('./tmp/')

# Save the image in a widely supported format (e.g., PNG)
imageio.imwrite('./tmp/gradient_image.png', image)

print("Image saved in './tmp/gradient_image.png'")