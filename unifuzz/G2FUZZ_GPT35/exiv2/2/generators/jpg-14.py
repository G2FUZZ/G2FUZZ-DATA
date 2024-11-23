import numpy as np
from PIL import Image

# Create a random image
image_data = np.random.randint(0, 256, (256, 256, 3), dtype=np.uint8)
image = Image.fromarray(image_data)

# Save the image with JPEG format and apply Chroma subsampling and Huffman encoding
image.save('./tmp/compressed_image_huffman.jpg', subsampling='4:2:0', quality=90, optimize=True, progressive=True, entropy_mode='o')

print("JPEG file with Chroma subsampling, Progressive mode, and Huffman encoding generated and saved successfully.")