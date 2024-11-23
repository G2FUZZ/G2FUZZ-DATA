import numpy as np
from PIL import Image

# Create a random image data
image_data = np.random.randint(0, 256, size=(100, 100, 3), dtype=np.uint8)

# Create a PIL Image object
image = Image.fromarray(image_data)

# Save the image as a JPG file
image.save('./tmp/generated_image.jpg')