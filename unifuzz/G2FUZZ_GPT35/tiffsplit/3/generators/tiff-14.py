import numpy as np
from PIL import Image

# Create a list to store multiple image data
images = []

# Generate multiple image data and alpha channel data
for _ in range(5):
    image_data = np.random.randint(0, 255, size=(256, 256), dtype=np.uint8)
    alpha_data = np.random.randint(0, 255, size=(256, 256), dtype=np.uint8)
    images.append(Image.fromarray(np.dstack((image_data, alpha_data))))

# Save the images as a multipage tiff file
images[0].save('./tmp/multipage_images.tiff', save_all=True, append_images=images[1:], compression='tiff_deflate', tile=(128, 128))