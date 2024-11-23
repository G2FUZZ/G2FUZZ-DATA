import numpy as np
from PIL import Image

# Create a random image
image_data = np.random.randint(0, 256, (100, 100, 3), dtype=np.uint8)
image = Image.fromarray(image_data)

# Save the image with custom quality settings
quality_settings = 80  # Adjust the quality settings here
image.save("./tmp/custom_quality.jpg", quality=quality_settings)