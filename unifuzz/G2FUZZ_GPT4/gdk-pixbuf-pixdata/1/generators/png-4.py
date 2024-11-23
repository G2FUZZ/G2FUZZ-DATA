import numpy as np
from PIL import Image

# Generate an example image
width, height = 256, 256
data = np.zeros((height, width, 3), dtype=np.uint8)

# Create a gradient
for i in range(height):
    for j in range(width):
        data[i, j] = [i % 256, j % 256, (i+j) % 256]

# Convert the numpy array to PIL Image
image = Image.fromarray(data)

# Save the image with Adam7 interlacing
image.save('./tmp/interlaced_image.png', 'PNG', interlace=True)