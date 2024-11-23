import numpy as np
from PIL import Image

# Create a white image
image_data = np.ones((100, 100, 3), dtype=np.uint8) * 255
image = Image.fromarray(image_data)

# Save the image as jpg file
image.save("./tmp/compatibility.jpg")