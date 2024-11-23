import numpy as np
from PIL import Image

# Create a random image data
image_data = np.random.randint(0, 256, size=(100, 100, 3), dtype=np.uint8)
image = Image.fromarray(image_data)

# Save the image with .jpg extension
image.save('./tmp/generated_image.jpg')