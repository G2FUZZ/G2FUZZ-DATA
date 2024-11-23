from PIL import Image
import numpy as np
import os

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Create a sample image using numpy
width, height = 256, 256
data = np.zeros((height, width, 3), dtype=np.uint8)
# Generate some patterns
data[64:192, 64:192] = [255, 0, 0]  # Red square
data[128:160, 128:160] = [0, 255, 0]  # Green square

# Convert numpy array to PIL Image
image = Image.fromarray(data)

# Define compression options with an additional JPEG 2000 Compression
compression_options = {
    'lzw': 'LZW',
    'jpeg': 'JPEG',
    'deflate': 'Deflate',
    'jpeg2000': 'JPEG2000'  # JPEG 2000 Compression
}

# Save the image with different compression schemes
for comp_scheme, pil_comp_scheme in compression_options.items():
    filename = f'./tmp/sample_{comp_scheme}.tiff'
    image.save(filename, format='TIFF', compression=pil_comp_scheme)
    print(f'Saved {filename} with {comp_scheme} compression.')