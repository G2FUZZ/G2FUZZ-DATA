import numpy as np
from PIL import Image

# Create a random image
image_data = np.random.randint(0, 255, (256, 256, 3), dtype=np.uint8)
image = Image.fromarray(image_data)

# Save the image as a jpg file with lossy compression
image.save('./tmp/lossy_compression.jpg', quality=95)