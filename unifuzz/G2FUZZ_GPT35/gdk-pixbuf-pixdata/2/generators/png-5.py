import numpy as np
from PIL import Image

# Create a low-resolution image
low_res_data = np.random.randint(0, 256, (100, 100, 3), dtype=np.uint8)
low_res_img = Image.fromarray(low_res_data)
low_res_img.save('./tmp/low_res_image.png')

# Create a high-resolution image
high_res_data = np.random.randint(0, 256, (500, 500, 3), dtype=np.uint8)
high_res_img = Image.fromarray(high_res_data)
high_res_img.save('./tmp/high_res_image.png')

# Combine low and high-resolution images for progressive rendering
progressive_img = Image.new('RGB', (500, 500))
progressive_img.paste(low_res_img, (0, 0))
progressive_img.save('./tmp/progressive_image.png')