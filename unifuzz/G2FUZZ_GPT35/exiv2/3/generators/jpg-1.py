import numpy as np
from PIL import Image

# Create a random RGB image
width = 100
height = 100
image_data = np.random.randint(0, 256, (height, width, 3), dtype=np.uint8)
image = Image.fromarray(image_data, 'RGB')

# Save the image as a JPEG file
image.save('./tmp/generated_image.jpg')