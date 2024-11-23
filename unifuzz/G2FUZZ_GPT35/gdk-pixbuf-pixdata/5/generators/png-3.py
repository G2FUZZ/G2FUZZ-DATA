import numpy as np
from PIL import Image

# Create an array with random pixel values for demonstration
width, height = 256, 256
image_array = np.random.randint(0, 256, (height, width, 3), dtype=np.uint8)

# Create and save PNG files with different color depths
color_depths = [1, 2, 4, 8, 16]

for depth in color_depths:
    image = Image.fromarray(image_array)
    image.save(f"./tmp/image_depth_{depth}.png", bit=depth)