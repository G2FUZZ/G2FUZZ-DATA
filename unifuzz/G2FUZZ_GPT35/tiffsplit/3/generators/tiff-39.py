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

# Create new images
base_image = Image.new('RGB', (300, 300), (255, 0, 0))
transparent_image = Image.new('RGBA', (300, 300), (0, 255, 0, 128))
cmyk_image = Image.new('CMYK', (300, 300), (0, 0, 0, 0))

# Save the images as layers in a multi-layer TIFF file with compression
with Image.new('RGB', (300, 300)) as multi_layer_image:
    multi_layer_image.save('./tmp/multi_layer_image_with_custom_tags.tiff', compression='tiff_adobe_deflate', save_all=True, append_images=[base_image, transparent_image, cmyk_image])