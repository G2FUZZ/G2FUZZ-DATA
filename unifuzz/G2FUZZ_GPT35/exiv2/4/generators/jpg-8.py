import numpy as np
from PIL import Image

# Create an image with complex color gradients
width, height = 800, 600
image = np.zeros((height, width, 3), dtype=np.uint8)
for y in range(height):
    for x in range(width):
        r = int(255 * x / width)
        g = int(255 * y / height)
        b = int(255 * np.sin(x * y / 10000))
        image[y, x] = [r, g, b]

# Save the image as a jpg file
file_path = './tmp/complex_color_gradients.jpg'
Image.fromarray(image).save(file_path)
print(f"Image saved at: {file_path}")