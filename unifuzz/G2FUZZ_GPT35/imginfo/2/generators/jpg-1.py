import numpy as np
from PIL import Image

# Create a black image
image_data = np.zeros((100, 100, 3), dtype=np.uint8)
image = Image.fromarray(image_data)

# Save the image in JPEG format
image.save("./tmp/black_image.jpg")