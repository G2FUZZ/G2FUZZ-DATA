import numpy as np
from PIL import Image

# Generate a random image
image_data = np.random.randint(0, 255, size=(300, 300, 3), dtype=np.uint8)
image = Image.fromarray(image_data)

# Save the image with quality settings
quality_values = [50, 70, 90]
for i, quality in enumerate(quality_values):
    image.save(f'./tmp/image_quality_{quality}.jpg', quality=quality)