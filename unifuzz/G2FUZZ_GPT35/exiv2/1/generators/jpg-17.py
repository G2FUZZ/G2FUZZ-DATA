import numpy as np
from PIL import Image

# Create a random image
image_data = np.random.randint(0, 255, (256, 256, 3), dtype=np.uint8)
image = Image.fromarray(image_data)

# Save the image as a jpg file with lossy compression
image.save('./tmp/lossy_compression_with_editing_compat.jpg', quality=80, dpi=(300, 300))