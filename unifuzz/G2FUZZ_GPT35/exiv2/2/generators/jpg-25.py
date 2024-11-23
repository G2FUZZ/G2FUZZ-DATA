import numpy as np
from PIL import Image

# Create a simple image with a pattern to demonstrate JPEG compression artifacts
image_data = np.zeros((100, 100, 3), dtype=np.uint8)
image_data[::10, ::10] = [255, 255, 255]  # Add a white pattern

# Save the image as a JPEG file with restart markers and different quality settings
restart_interval = 5  # Set the restart marker interval
for quality in range(1, 11):
    image = Image.fromarray(image_data)
    image.save(f'./tmp/compression_artifacts_q{quality}_restart.jpg', quality=quality * 10, 
               dpi=(300, 300), restart_interval=restart_interval)