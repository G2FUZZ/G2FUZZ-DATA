import numpy as np
from PIL import Image

# Create a 100x100 black image
image_data = np.zeros((100, 100, 3), dtype=np.uint8)
image_data.fill(0)

# Create PIL image
image = Image.fromarray(image_data, 'RGB')

# Save image as jpg file
image.save('./tmp/example.jpg')