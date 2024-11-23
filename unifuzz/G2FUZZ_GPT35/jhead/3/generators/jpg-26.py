import numpy as np
from PIL import Image

# Create a random image
image_data = np.random.randint(0, 256, (100, 100, 3), dtype=np.uint8)
image = Image.fromarray(image_data)

# Add metadata information to the image
metadata = {
    "author": "John Doe",
    "date_created": "2022-09-15",
    "description": "Random image with custom metadata"
}

for key, value in metadata.items():
    image.info[key] = value

# Save the image with custom quality settings and metadata
quality_settings = 80  # Adjust the quality settings here
image.save("./tmp/custom_metadata.jpg", quality=quality_settings)