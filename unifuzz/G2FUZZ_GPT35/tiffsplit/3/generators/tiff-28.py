import numpy as np
from PIL import Image
import tifffile

# Create an array with random pixel values for image 1
image1 = np.random.randint(0, 255, (256, 256, 3), dtype=np.uint8)

# Create an array with random pixel values for image 2
image2 = np.random.randint(0, 255, (256, 256, 3), dtype=np.uint8)

# Save the images as TIFF files with multiple pages and software-specific extensions
with Image.new('RGB', (256, 256)) as img:
    img.putdata([tuple(pixel) for row in image1 for pixel in row])
    img.save('./tmp/multi_page_with_extension.tiff')

with Image.open('./tmp/multi_page_with_extension.tiff') as img:
    img.putdata([tuple(pixel) for row in image2 for pixel in row])
    img.save('./tmp/multi_page_with_extension.tiff', append=True)

# Add software-specific extensions using tifffile library
with Image.open('./tmp/multi_page_with_extension.tiff') as img:
    with tifffile.TiffWriter('./tmp/multi_page_with_extension_with_extensions.tiff') as tif:
        for i in range(img.n_frames):
            img.seek(i)
            tif.save(img, software='MySoftware', description='Software-specific Extensions: TIFF files can have extensions specific to certain software applications for additional functionality.')