import numpy as np
from PIL import Image

# Create a 100x100 RGBA image with random values
data = np.random.randint(0, 255, (100, 100, 4), dtype=np.uint8)
img = Image.fromarray(data, 'RGBA')

# Create a thumbnail image
thumbnail_size = (50, 50)
thumbnail_data = np.random.randint(0, 255, (50, 50, 4), dtype=np.uint8)
thumbnail_img = Image.fromarray(thumbnail_data, 'RGBA')
thumbnail_img.thumbnail(thumbnail_size)

# Add the thumbnail image as a TIFF tag
img_info = img.info
img_info[0x501B] = thumbnail_img.tobytes()

# Save the image with alpha channel and thumbnail image as a TIFF file
img.save('./tmp/alpha_channel_with_thumbnail.tiff', tiffinfo=img_info)