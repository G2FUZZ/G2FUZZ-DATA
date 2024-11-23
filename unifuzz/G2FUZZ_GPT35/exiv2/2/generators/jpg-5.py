import numpy as np
from PIL import Image

# Create a white image
width, height = 100, 100
data = np.ones((height, width, 3), dtype=np.uint8) * 255
image = Image.fromarray(data)

# Save the image as jpg in ./tmp/ directory
image.save("./tmp/compatibility.jpg")