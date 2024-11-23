import numpy as np
from PIL import Image

# Create a white image
white_image = Image.fromarray(np.ones((100, 100, 3), dtype=np.uint8) * 255)

# Save the image with .jpg extension
white_image.save("./tmp/white_image.jpg")