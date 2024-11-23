import numpy as np
from PIL import Image
import jpegio

# Creating a sample image (you can replace this with your own image generation logic)
image_data = np.random.randint(0, 255, size=(256, 256, 3), dtype=np.uint8)
image = Image.fromarray(image_data)

# Save the image in JPEG format with DCT compression and Huffman encoding
image.save('./tmp/compressed_image_huffman.jpg', quality=95, subsampling=0)

# Read the saved image
jpeg_struct = jpegio.read('./tmp/compressed_image_huffman.jpg')