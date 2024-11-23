import numpy as np
from PIL import Image

# Create an array of random pixels for each page
num_pages = 5
image_size = (100, 100)
images = [np.random.randint(0, 255, size=(image_size[1], image_size[0], 3), dtype=np.uint8) for _ in range(num_pages)]

# Save the images as a multi-page TIFF file in BigTIFF format
with Image.new('RGB', image_size, (0, 0, 0)) as img:
    img.save('./tmp/multi_page_bigtiff.tiff', save_all=True, append_images=[Image.fromarray(page) for page in images], bigtiff=True)