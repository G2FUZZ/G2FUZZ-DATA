import numpy as np
from PIL import Image

# Generate a simple image
image_array = np.zeros((100, 100, 3), dtype=np.uint8)
image_array[:, :50] = [255, 0, 0]  # Left half is red
image_array[:, 50:] = [0, 0, 255]  # Right half is blue

# Create and save the image as PNG
image = Image.fromarray(image_array)
image.save('./tmp/optimized_image.png')