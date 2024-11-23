from PIL import Image
from tifffile import TiffWriter

# Create a new TIFF image with multiple layers and custom tags
image = Image.new('RGBA', (400, 400))  # RGBA mode for alpha channel
layer1 = Image.new('RGBA', (400, 400), color=(255, 0, 0, 128))  # Red semi-transparent layer
layer2 = Image.new('RGBA', (400, 400), color=(0, 255, 0, 128))  # Green semi-transparent layer

# Define custom tags
custom_tags = {
    '65000': 'Custom Tag Example',
    '65001': 42,
    '65002': 'Extra Information',
    '65003': (1.234, 5.678)
}

# Save the image with custom tags, multiple layers, and tiled organization
with TiffWriter('./tmp/complex_tiff_file.tiff') as tif:
    tif.save(image, metadata=custom_tags, tile=(128, 128))  # Tiled organization
    tif.save(layer1, tile=(128, 128))
    tif.save(layer2, tile=(128, 128))