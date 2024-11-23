import numpy as np
from PIL import Image
import subprocess

# Create a random image as an example
image_data = np.random.randint(0, 255, size=(100, 100, 3), dtype=np.uint8)
image = Image.fromarray(image_data)

# Save the image as a jpg file in the './tmp/' directory
image.save('./tmp/generated_image.jpg')

# Convert the generated jpg image to WebP format
subprocess.call(['cwebp', './tmp/generated_image.jpg', '-o', './tmp/generated_image.webp'])