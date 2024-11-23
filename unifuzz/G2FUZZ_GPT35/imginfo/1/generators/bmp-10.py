import numpy as np
from PIL import Image

# Create a new BMP file
image_data = np.array([[10]], dtype=np.uint8)
image = Image.fromarray(image_data, mode='L')
image.save('./tmp/versatility.bmp')