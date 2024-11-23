import numpy as np
from PIL import Image
from tifffile import imwrite

# Create an Image Masking example
mask_data = np.random.randint(0, 2, (300, 300), dtype=np.uint8) * 255
mask_image = Image.fromarray(mask_data, 'L')

# Add custom tags for the TIFF file
custom_tags = {
    10: b"Custom Tags: TIFF files can include custom tags for specific application requirements.",
    317: b"Image Compression Options: TIFF files can offer various compression options such as PackBits, CCITT Group 3/4, or Deflate."
}

# Save the image with custom tags
imwrite('./tmp/mask_image_with_custom_tags.tiff', mask_data, description=custom_tags[10], extratags=[(317, 's', 1, custom_tags[317])])