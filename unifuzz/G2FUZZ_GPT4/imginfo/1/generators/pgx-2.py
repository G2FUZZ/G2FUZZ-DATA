from PIL import Image
import numpy as np
import os
from glymur import Jp2k

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Create a sample image (e.g., 256x256 pixels, grayscale)
width, height = 256, 256
data = np.random.randint(0, 255, (height, width)).astype('uint8')

# Define the path for the JP2 file
jp2_file_path = './tmp/sample_image.jp2'

# Save the numpy array as a JP2 file with high compression
jp2 = Jp2k(jp2_file_path, data=data, cratios=[50])  # cratios=[50] implies a high compression ratio

print(f"JP2 file saved at: {jp2_file_path}")