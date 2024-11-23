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

# Define compression options
compression_options = {
    'lzw': 'LZW',
    'jpeg': 'JPEG',
    'deflate': 'Deflate'
}

# Save the image with different compression schemes
for comp_scheme, pil_comp_scheme in compression_options.items():
    filename = f'./tmp/sample_{comp_scheme}.tiff'
    # Including halftoning information
    image.save(filename, format='TIFF', compression=pil_comp_scheme, tiffinfo={317: 1})
    print(f'Saved {filename} with {comp_scheme} compression and halftoning information.')