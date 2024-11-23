import numpy as np
from PIL import Image

# Create an array with random pixel values for image 1
image1 = np.random.randint(0, 255, (256, 256, 3), dtype=np.uint8)

# Create an array with random pixel values for image 2
image2 = np.random.randint(0, 255, (256, 256, 3), dtype=np.uint8)

# Save the images as TIFF files with multiple pages
with Image.new('RGB', (256, 256)) as img:
    img.putdata([tuple(pixel) for row in image1 for pixel in row])
    img.save('./tmp/multi_page.tiff')

with Image.open('./tmp/multi_page.tiff') as img:
    img.putdata([tuple(pixel) for row in image2 for pixel in row])
    img.save('./tmp/multi_page.tiff', append=True)