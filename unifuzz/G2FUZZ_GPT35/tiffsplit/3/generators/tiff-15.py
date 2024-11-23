import numpy as np
from PIL import Image

# Create an Image Masking example
mask_data = np.random.randint(0, 2, (300, 300), dtype=np.uint8) * 255
mask_image = Image.fromarray(mask_data, 'L')
mask_image.save('./tmp/mask_image.tiff')