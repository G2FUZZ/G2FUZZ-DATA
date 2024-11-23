import numpy as np
from PIL import Image

# Create a random image
image_data = np.random.randint(0, 256, (256, 256, 3), dtype=np.uint8)
image = Image.fromarray(image_data)

# Save the image with JPEG format and apply Chroma subsampling
image.save('./tmp/compressed_image_subsampling.jpg', subsampling='4:2:0', quality=90, optimize=True, progressive=True)

print("JPEG file with Chroma subsampling and Progressive mode generated and saved successfully.")