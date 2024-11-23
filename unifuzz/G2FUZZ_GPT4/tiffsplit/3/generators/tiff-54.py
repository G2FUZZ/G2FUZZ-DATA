import numpy as np
from PIL import Image, TiffTags, TiffImagePlugin
import os

def create_gradient_image_data(width, height):
    """Create a numpy array with a gradient effect for image creation."""
    array = np.zeros((height, width, 3), dtype=np.uint8)
    for i in range(height):
        for j in range(width):
            array[i, j] = [i % 256, j % 256, (i+j) % 256]
    return array

def save_multipage_tiff_with_custom_tags(output_path, images_data, compression_methods, reference_black_white):
    """
    Save multiple images as a multi-page TIFF with custom tags.

    Parameters:
    - output_path: Path to save the TIFF file.
    - images_data: A list of numpy arrays representing images.
    - compression_methods: A list of compression methods for each page.
    - reference_black_white: Placeholder values for black and white points.
    """
    # Initialize a list to hold PIL Image objects
    image_objects = [Image.fromarray(image_data) for image_data in images_data]
    
    custom_tags = {
        532: (reference_black_white, TiffTags.FLOAT)  # 532 is the tag for ReferenceBlackWhite
    }
    
    # Use TiffImagePlugin to add the custom tags and save the images
    with TiffImagePlugin.AppendingTiffWriter(output_path, True) as tf:
        for i, image in enumerate(image_objects):
            info = {
                'compression': compression_methods[i],
                'custom_tiff_tags': custom_tags
            }
            image.save(tf, **info)
            tf.newFrame()

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Create image data for three gradient images
image_data1 = create_gradient_image_data(256, 256)
image_data2 = create_gradient_image_data(256, 256)
image_data3 = create_gradient_image_data(256, 256)

# List of images data
images_data = [image_data1, image_data2, image_data3]

# List of compression methods for each page
compression_methods = ['tiff_lzw', 'jpeg', 'tiff_adobe_deflate']

# Placeholder values for black and white points
reference_black_white = (0, 255, 0, 255, 0, 255)

# Output path for the multi-page TIFF
output_path = './tmp/sample_multipage_with_custom_tags.tiff'

# Save the multi-page TIFF with custom tags
save_multipage_tiff_with_custom_tags(output_path, images_data, compression_methods, reference_black_white)

print(f"Multi-page TIFF with custom tags saved to {output_path}")