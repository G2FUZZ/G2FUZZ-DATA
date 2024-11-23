import os
from PIL import Image
import numpy as np

# Create a temporary directory if it doesn't exist
tmp_dir = './tmp/'
os.makedirs(tmp_dir, exist_ok=True)

# Image size
width, height = 100, 100

# Create an array of red pixels
data = np.zeros((height, width, 3), dtype=np.uint8)
data[:, :] = [255, 0, 0]  # Red color

# Create an image from the array
image = Image.fromarray(data)

# Save the image as a PNG file
file_path = os.path.join(tmp_dir, 'portability_feature.png')
image.save(file_path, format='PNG')

print(f"PNG file saved to {file_path}")