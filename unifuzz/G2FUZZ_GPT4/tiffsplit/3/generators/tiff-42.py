import numpy as np
import os
from PIL import Image
import tifffile as tiff

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

def create_gradient_image(width, height, channels=3):
    """Create a gradient image array."""
    array = np.zeros((height, width, channels), dtype=np.uint8)
    for i in range(height):
        for j in range(width):
            if channels == 1:
                # For single-channel images, assign a single value
                array[i, j, 0] = (i + j) % 256
            else:
                # For multi-channel images, assign values to all channels
                array[i, j, :] = [i % 256, j % 256, (i+j) % 256]
    return array

# Create sample images with gradients
width, height = 256, 256
img1 = create_gradient_image(width, height)
img2 = create_gradient_image(width, height, 1)  # Single channel
img3 = create_gradient_image(width, height)

# Using tifffile to write a sequence of images with different compressions
with tiff.TiffWriter('./tmp/complex_structure.tiff', bigtiff=True) as tif:
    # Image 1 with Deflate compression as a workaround
    tif.write(img1, compression='deflate')
    
    # Image 2 with JPEG compression (single channel image has to be saved differently)
    img2_pil = Image.fromarray(img2.squeeze())  # Squeeze to remove the single channel dimension for PIL
    img2_pil_path = './tmp/temp_img2.tiff'
    img2_pil.save(img2_pil_path, compression='jpeg')
    img2_pil_tiff = tiff.imread(img2_pil_path)
    tif.write(img2_pil_tiff, compression='jpeg')
    os.remove(img2_pil_path)  # Clean up the temporary file
    
    # Image 3 with Deflate compression
    tif.write(img3, compression='deflate')

print("TIFF file with complex structure has been created in './tmp/'.")