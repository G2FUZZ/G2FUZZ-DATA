import numpy as np
from PIL import Image
import os

# Ensure the ./tmp/ directory exists
if not os.path.exists('./tmp/'):
    os.makedirs('./tmp/')

# Generate an image with random colors
width, height = 256, 256
array = np.random.rand(height, width, 3) * 255
image = Image.fromarray(array.astype('uint8')).convert('RGB')

# Save the image with different levels of compression
# Higher 'quality' values mean less compression and better image quality
# Lower 'quality' values mean more compression and lower image quality
compression_levels = [95, 50, 10]  # Example compression levels

for i, quality in enumerate(compression_levels):
    filename = f'./tmp/random_image_quality_{quality}.jpg'
    image.save(filename, 'JPEG', quality=quality)