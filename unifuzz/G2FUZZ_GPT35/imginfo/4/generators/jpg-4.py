import numpy as np
from PIL import Image

# Create a low-resolution image
low_res_image = np.random.randint(0, 256, size=(100, 100, 3), dtype=np.uint8)
low_res_image = Image.fromarray(low_res_image)
low_res_image.save('./tmp/low_res_image.jpg', format='JPEG', subsampling=0, quality=95, optimize=True, progressive=True)