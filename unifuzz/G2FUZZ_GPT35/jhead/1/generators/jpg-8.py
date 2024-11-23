import numpy as np
from PIL import Image

# Create a simple white image
image = Image.fromarray(np.ones((100, 100, 3), dtype=np.uint8) * 255)

# Save the image as a jpg file
image.save('./tmp/white_image.jpg')