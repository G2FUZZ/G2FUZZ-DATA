import numpy as np
from PIL import Image

# Create a gradient image
width, height = 256, 256
image = np.zeros((height, width, 3), dtype=np.uint8)
for x in range(width):
    image[:, x] = [x, x, x]

# Create a PIL Image object
img = Image.fromarray(image)

# Set interlace to True for progressive rendering
img.save("./tmp/interlaced.png", interlace=True)