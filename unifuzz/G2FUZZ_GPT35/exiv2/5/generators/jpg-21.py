import numpy as np
from PIL import Image

# Creating a sample image (you can replace this with your own image generation logic)
image_data = np.random.randint(0, 255, size=(256, 256, 3), dtype=np.uint8)
image = Image.fromarray(image_data)

# Adding embedded thumbnail data
thumbnail_data = np.random.randint(0, 255, size=(64, 64, 3), dtype=np.uint8)
thumbnail_image = Image.fromarray(thumbnail_data)
thumbnail_bytes = thumbnail_image.tobytes()

# Save the image in JPEG format with DCT compression, Chroma subsampling, Progressive display, and Embedded thumbnails
image.save('./tmp/compressed_image_with_thumbnail.jpg', format='JPEG', quality=95, subsampling='4:2:0', progressive=True, thumbnail=thumbnail_bytes)