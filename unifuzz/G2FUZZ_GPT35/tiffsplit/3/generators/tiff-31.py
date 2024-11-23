import numpy as np
from PIL import Image

# Create a 2D numpy array to represent the image data
image_data = np.random.randint(0, 255, size=(256, 256), dtype=np.uint8)

# Create alpha channel data (transparency values)
alpha_data = np.random.randint(0, 255, size=(256, 256), dtype=np.uint8)

# Create image metadata
metadata = {
    270: "Example Image Description",  # Tag number for ImageDescription
    305: "Python PIL",  # Tag number for Software
    306: "2023:01:01 12:00:00",  # Tag number for DateTime
    37510: "Added brightness adjustment",  # Tag number for ImageEditingHistory
}

# Save the image data and alpha channel data as a multi-layer TIFF file with LZW compression
images_to_save = [Image.fromarray(np.dstack((image_data, alpha_data)))]

for _ in range(4):  # Add 3 more layers for demonstration
    random_image_data = np.random.randint(0, 255, size=(256, 256), dtype=np.uint8)
    random_alpha_data = np.random.randint(0, 255, size=(256, 256), dtype=np.uint8)
    images_to_save.append(Image.fromarray(np.dstack((random_image_data, random_alpha_data))) )

with Image.new('RGBA', (1, 1)) as tmp_image:
    for idx, img in enumerate(images_to_save):
        tmp_image.paste(img, (0, 0))
        tmp_image.save(f'./tmp/multi_layer_image_{idx}.tiff', save_all=True, compression='tiff_lzw', tiffinfo=metadata, tile=(128, 128))