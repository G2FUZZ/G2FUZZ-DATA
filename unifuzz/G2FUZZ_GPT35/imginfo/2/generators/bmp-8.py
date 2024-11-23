import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

# Create a 100x100 numpy array with random values representing the image
image_data = np.random.randint(0, 256, (100, 100, 3), dtype=np.uint8)

# Create an image from the numpy array
image = Image.fromarray(image_data)

# Save the image in BMP format to the specified directory
image.save('./tmp/compatibility.bmp')