from PIL import Image
from tifffile import TiffWriter

# Create a new TIFF image with multiple layers
image = Image.new('RGBA', (200, 200))  # RGBA mode for alpha channel
layer1 = Image.new('RGBA', (200, 200), color=(255, 0, 0, 128))  # Red semi-transparent layer
layer2 = Image.new('RGBA', (200, 200), color=(0, 255, 0, 128))  # Green semi-transparent layer

# Add metadata information
metadata = {
    'Author': 'Jane Smith',
    'Copyright': '2022',
    'Creation Date': '2022-09-20',
    'Compression Options': 'LZW',
    'Layers and Alpha Channels': 'Supports multiple layers for image compositing',
    'Image Resolution': '300 dpi',
    'Color Profile': 'Adobe RGB (1998)',
    '700': 300,  # XResolution
    '701': 300  # YResolution
}

# Save the image with metadata and layers
with TiffWriter('./tmp/metadata_example_with_layers_resolution_profile.tiff') as tif:
    tif.save(image, metadata=metadata)
    tif.save(layer1)
    tif.save(layer2)