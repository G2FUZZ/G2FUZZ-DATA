import numpy as np
from PIL import Image

# Generate a sample image
image_size = (256, 256)
image_data = np.random.randint(0, 256, size=image_size, dtype=np.uint8)
sample_image = Image.fromarray(image_data)

# Save the sample image as a JPEG file with high compression
output_path = './tmp/artifact.jpg'
sample_image.save(output_path, quality=10)