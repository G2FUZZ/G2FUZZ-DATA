import numpy as np
from PIL import Image

# Create a simple image with some artifacts
image_data = np.random.randint(0, 255, size=(100, 100, 3), dtype=np.uint8)
image = Image.fromarray(image_data)

# Save the generated image as a jpg file
image.save('./tmp/artifact.jpg', 'JPEG', quality=10)