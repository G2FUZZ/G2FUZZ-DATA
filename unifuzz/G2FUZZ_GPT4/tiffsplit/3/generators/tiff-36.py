import numpy as np
from PIL import Image, TiffTags, TiffImagePlugin
import os

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Create a sample image - let's create a gradient image for demonstration
width, height = 256, 256
array = np.zeros((height, width, 3), dtype=np.uint8)

# Creating a gradient effect for demonstration purposes
for i in range(height):
    for j in range(width):
        array[i, j] = [i % 256, j % 256, (i+j) % 256]

# Reference Black White Tag - specifying values
# Assuming a typical use case, but you might need to adjust these values based on your requirements
reference_black_white = (0, 255, 0, 255, 0, 255)  # Placeholder values for black and white points

# Custom save function to include additional TIFF tags
def save_with_custom_tags(path, image, compression):
    # Define custom tags here. The key should be the tag number,
    # and the value should be a tuple of the value and type.
    # ReferenceBlackWhite tag number is 532
    custom_tags = {
        532: (reference_black_white, TiffTags.FLOAT)
    }
    
    # Fetch the existing info dict and update it with custom tags
    info = image.info
    info['compression'] = compression
    info['custom_tiff_tags'] = custom_tags
    
    # Use TiffImagePlugin to add the custom tags and save the image
    with TiffImagePlugin.AppendingTiffWriter(path, True) as tf:
        image.save(tf, **info)

# Save the same image with different compression schemes
compression_schemes = ['tiff_lzw', 'jpeg', 'tiff_adobe_deflate']

for compression in compression_schemes:
    img = Image.fromarray(array)
    save_with_custom_tags(f'./tmp/sample_{compression}_with_ref_bw.tiff', img, compression)