from PIL import Image
import numpy as np
import os

# Ensure the ./tmp/ directory exists
output_dir = './tmp/'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Create an image with random data to demonstrate lossless compression
# For demonstration purposes, we're creating a 256x256 grayscale image
image_data = np.random.randint(0, 256, (256, 256), dtype=np.uint8)

# Determine the minimum and maximum sample values
min_sample_value = np.min(image_data)
max_sample_value = np.max(image_data)

# Create an image object from the image_data
image = Image.fromarray(image_data)

# Save the image with lossless compression (using LZW compression)
output_path = os.path.join(output_dir, 'lossless_compression.tiff')
image.save(output_path, format='TIFF', compression='tiff_lzw')

print(f"Image saved to {output_path} with Minimum and Maximum Sample Values: {min_sample_value}, {max_sample_value}")