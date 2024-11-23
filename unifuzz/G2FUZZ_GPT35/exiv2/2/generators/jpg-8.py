import numpy as np
from PIL import Image

# Create a simple image with a pattern to demonstrate JPEG compression artifacts
image_data = np.zeros((100, 100, 3), dtype=np.uint8)
image_data[::10, ::10] = [255, 255, 255]  # Add a white pattern

# Save the image as a JPEG file with different quality settings to observe compression artifacts
for quality in range(1, 11):
    image = Image.fromarray(image_data)
    image.save(f'./tmp/compression_artifacts_q{quality}.jpg', quality=quality * 10)