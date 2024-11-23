import numpy as np
from PIL import Image, TiffImagePlugin
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

# List of compression schemes to demonstrate
compression_schemes = ['tiff_lzw', 'jpeg', 'tiff_adobe_deflate']

# Save the same image with different compression schemes
for compression in compression_schemes:
    img = Image.fromarray(array)
    if compression == 'tiff_lzw':  # Assuming we only add Ink Names Tag for the 'tiff_lzw' compression for demonstration
        # Prepare the TIFF tags including the Ink Names Tag (tag number 333)
        # This tag is a list of names; here we separate them with NUL characters as per TIFF spec
        ink_names = 'Cyan\0Magenta\0Yellow\0Black'
        tiff_info = TiffImagePlugin.ImageFileDirectory_v2()
        tiff_info[333] = ink_names
        
        # Save the TIFF with custom tags
        with TiffImagePlugin.AppendingTiffWriter(f'./tmp/sample_{compression}_with_ink_names.tiff', True) as tf:
            # Correctly pass the file object to the save method
            img.save(tf, format='TIFF', tiffinfo=tiff_info)
    else:
        img.save(f'./tmp/sample_{compression}.tiff', compression=compression)