from PIL import Image
import numpy as np
import os

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Create multiple images to be stored in a single TIFF file
image1 = Image.new('RGB', (100, 100), color = 'red')
image2 = Image.new('RGB', (100, 100), color = 'green')
image3 = Image.new('RGB', (100, 100), color = 'blue')

# Create a floating-point image
width, height = 100, 100
float_data = np.random.rand(height, width).astype('float32')

# Scale the floating-point data to the 0-255 range
scaled_data = (255 * (float_data - np.min(float_data)) / np.ptp(float_data)).astype('uint8')

# Replicate the scaled data across three channels to create an 'RGB' image
rgb_data = np.stack((scaled_data,)*3, axis=-1)

# Convert the RGB data to an 'RGB' image
image4 = Image.fromarray(rgb_data, 'RGB')

# Save the images as a multipage TIFF with JPEG Compression
image1.save('./tmp/multiple_images_with_float_data.tiff', save_all=True, compression="jpeg", append_images=[image2, image3, image4])

print("TIFF file with multiple images, including converted floating-point data, created successfully.")