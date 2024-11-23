import numpy as np
from PIL import Image

# Create a white image
image = np.ones((100, 100, 3), dtype=np.uint8) * 255
image = Image.fromarray(image)

# Save the image as a jpg file
image.save('./tmp/compatibility.jpg')