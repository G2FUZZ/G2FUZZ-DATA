import numpy as np
import imageio

# Generate a sample image
image_data = np.random.randint(0, 255, (512, 512, 3), dtype=np.uint8)

# Save the image as a 'tiff' file without compression
imageio.imwrite('./tmp/sample_image.tiff', image_data, format='TIFF-PIL')