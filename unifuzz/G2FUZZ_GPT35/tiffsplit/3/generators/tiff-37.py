import numpy as np
from PIL import Image
from PIL.TiffTags import TAGS_V2

# Create a 2D numpy array to represent the image data
image_data = np.random.randint(0, 255, size=(256, 256), dtype=np.uint8)

# Create alpha channel data (transparency values)
alpha_data = np.random.randint(0, 255, size=(256, 256), dtype=np.uint8)

# Create image metadata
metadata = {
    270: "Example Image Description",  # Tag number for ImageDescription
    305: "Python PIL",  # Tag number for Software
    306: "2023:01:01 12:00:00"  # Tag number for DateTime
}

# Create an image with metadata
image_with_metadata = Image.fromarray(np.dstack((image_data, alpha_data)))

# Create another image with different content
image_data2 = np.random.randint(0, 255, size=(256, 256), dtype=np.uint8)
alpha_data2 = np.random.randint(0, 255, size=(256, 256), dtype=np.uint8)
image_with_metadata2 = Image.fromarray(np.dstack((image_data2, alpha_data2)))

# Create a list of images to be saved in the multi-layer TIFF file
images_to_save = [image_with_metadata, image_with_metadata2]

# Save the images as a multi-layer TIFF file with LZW compression and metadata
with Image.new('RGBA', (1, 1)) as tmp_image:
    for idx, img in enumerate(images_to_save):
        tmp_image.paste(img, (0, 0))
        tmp_image.save(f'./tmp/multi_layer_image_with_metadata_{idx}.tiff', save_all=True, compression='tiff_lzw', tile=(128, 128), tiffinfo=metadata, bigtiff=True)