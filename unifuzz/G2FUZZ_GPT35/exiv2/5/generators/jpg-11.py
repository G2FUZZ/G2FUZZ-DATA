import numpy as np
from PIL import Image

# Creating a sample image (you can replace this with your own image generation logic)
image_data = np.random.randint(0, 255, size=(256, 256, 3), dtype=np.uint8)
image = Image.fromarray(image_data)

# Save the image in JPEG format with DCT compression and Chroma subsampling
image.save('./tmp/compressed_image_subsampling.jpg', quality=95, subsampling='4:2:0')