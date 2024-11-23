import os
from PIL import Image
import numpy as np
import zlib
import json

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Generate data for pixdata files

# Example image data: A simple gradient
width, height = 256, 256
image_data = np.zeros((height, width, 3), dtype=np.uint8)
for y in range(height):
    for x in range(width):
        image_data[y, x] = [x, y, (x+y) % 256]  # RGB channels

# Save the image using different compression options
# PNG (lossless)
png_filename = './tmp/gradient_lossless.png'
Image.fromarray(image_data).save(png_filename, format='PNG')

# JPEG (lossy, with varying quality levels)
jpeg_filename_high_quality = './tmp/gradient_lossy_high_quality.jpg'
jpeg_filename_low_quality = './tmp/gradient_lossy_low_quality.jpg'
Image.fromarray(image_data).save(jpeg_filename_high_quality, format='JPEG', quality=95)
Image.fromarray(image_data).save(jpeg_filename_low_quality, format='JPEG', quality=25)

# Optionally, demonstrate saving a compressed representation of some data in a custom format
# For simplicity, we'll compress a simple JSON structure
data_to_compress = {
    'description': 'Example of compressed data',
    'content': 'This is a simple text to demonstrate compression in a custom pixdata file.'
}
compressed_data = zlib.compress(json.dumps(data_to_compress).encode('utf-8'))

# Save the compressed data to a file
compressed_filename = './tmp/example_compressed.pixdata'
with open(compressed_filename, 'wb') as file:
    file.write(compressed_data)

print("Generated pixdata files with varying compression methods.")