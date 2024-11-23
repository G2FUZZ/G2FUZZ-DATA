import numpy as np
from PIL import Image

# Create a white image of size 100x100
white_image = np.ones((100, 100, 3), dtype=np.uint8) * 255
image = Image.fromarray(white_image)

# Save the image as .jpg file
image.save('./tmp/white_image.jpg')