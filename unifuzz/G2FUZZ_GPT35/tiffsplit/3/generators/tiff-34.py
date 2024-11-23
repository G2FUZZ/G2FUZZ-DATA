import numpy as np
from PIL import Image

# Create a list to store multiple image data
images = []

# Generate multiple image data and alpha channel data
for _ in range(5):
    image_data = np.random.randint(0, 255, size=(256, 256), dtype=np.uint8)
    alpha_data = np.random.randint(0, 255, size=(256, 256), dtype=np.uint8)
    images.append(Image.fromarray(np.dstack((image_data, alpha_data))))

# Create a list of images to be saved in the TIFF file
images_to_save = images

# Save the images as a multi-layer TIFF file with LZW compression
with Image.new('RGBA', (1, 1)) as tmp_image:
    for idx, img in enumerate(images_to_save):
        tmp_image.paste(img, (0, 0))
        tmp_image.save(f'./tmp/multi_layer_tiff_{idx}.tiff', save_all=True, compression='tiff_lzw')