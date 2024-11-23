import numpy as np
from PIL import Image

# Create a random image as an example
image_data = np.random.randint(0, 255, size=(100, 100, 3), dtype=np.uint8)
image = Image.fromarray(image_data)

# Save the image as a jpg file in the './tmp/' directory with progressive display support
image.save('./tmp/generated_image.jpg', format='JPEG', quality=95, optimize=True, progressive=True)