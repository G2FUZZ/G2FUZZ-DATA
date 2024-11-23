import numpy as np
from PIL import Image

# Create a white image
width, height = 100, 100
image_data = np.ones((height, width, 3), dtype=np.uint8) * 255
image = Image.fromarray(image_data)

# Save the image as a jpg file
image.save('./tmp/compatibility.jpg')